from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Count

from .models import Post, Like, Comment, Follow
from .forms import RegisterForm, PostForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "core/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            error = "Invalid username or password!"

    return render(request, "core/login.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def home(request):
    form = PostForm()

    posts = Post.objects.all().order_by("-created_at").annotate(
        like_count=Count("likes"),
        comment_count=Count("comments")
    )

    liked_post_ids = Like.objects.filter(user=request.user).values_list("post_id", flat=True)

    suggested_users = User.objects.exclude(id=request.user.id)[:6]

    followers_count = Follow.objects.filter(following=request.user).count()
    following_count = Follow.objects.filter(follower=request.user).count()
    posts_count = Post.objects.filter(user=request.user).count()

    return render(request, "core/home.html", {
        "form": form,
        "posts": posts,
        "liked_post_ids": liked_post_ids,
        "suggested_users": suggested_users,
        "followers_count": followers_count,
        "following_count": following_count,
        "posts_count": posts_count
    })


@login_required
@require_POST
def create_post(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
    return redirect("home")


@login_required
@require_POST
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like_obj = Like.objects.filter(user=request.user, post=post)
    if like_obj.exists():
        like_obj.delete()
        liked = False
    else:
        Like.objects.create(user=request.user, post=post)
        liked = True

    return JsonResponse({
        "liked": liked,
        "like_count": post.likes.count()
    })


@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    text = request.POST.get("text", "").strip()

    if not text:
        return JsonResponse({"success": False})

    comment = Comment.objects.create(
        post=post,
        user=request.user,
        text=text
    )

    return JsonResponse({
        "success": True,
        "comment_count": post.comments.count(),
        "comment": {
            "username": comment.user.username,
            "text": comment.text,
        }
    })



@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(user=profile_user).order_by("-created_at").annotate(
        like_count=Count("likes"),
        comment_count=Count("comments")
    )

    followers_count = Follow.objects.filter(following=profile_user).count()
    following_count = Follow.objects.filter(follower=profile_user).count()
    posts_count = Post.objects.filter(user=profile_user).count()

    is_following = False
    if request.user != profile_user:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(request, "core/profile.html", {
        "profile_user": profile_user,
        "posts": posts,
        "followers_count": followers_count,
        "following_count": following_count,
        "posts_count": posts_count,
        "is_following": is_following,
    })


@login_required
@require_POST
def toggle_follow(request, username):
    target_user = get_object_or_404(User, username=username)

    if target_user == request.user:
        return redirect("profile", username=username)

    follow_obj = Follow.objects.filter(follower=request.user, following=target_user)

    if follow_obj.exists():
        follow_obj.delete()
    else:
        Follow.objects.create(follower=request.user, following=target_user)

    return redirect("profile", username=username)

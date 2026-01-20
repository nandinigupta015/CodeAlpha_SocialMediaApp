from django.contrib.auth.models import User
from core.models import Post
import random


def run():
    dummy_users = [
        ("sarahj", "Sarah J"),
        ("mikewav", "Mike.wav"),
        ("cloudnine", "Emma ☁️"),
        ("alexzap", "Alex ⚡"),
        ("moonchild", "Lisa Moon"),
    ]

    dummy_posts = [
        "just coded for 6 hours straight and forgot to eat lunch... dev life hits different 💻✨",
        "golden hour really said 'let me make everything look magical' today 🌅",
        "starting my internship project today 😭 wish me luck!",
        "learning Django is honestly fun when things work 😭🔥",
        "made a glassmorphism UI today and i feel like a designer ✨",
        "debugging at 2 AM is a different vibe 💀",
        "consistency > motivation. day 1 done ✅",
    ]

    created_users = []

    # ✅ Create dummy users
    for username, fullname in dummy_users:
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password("12345678")  # common demo password
            user.first_name = fullname
            user.save()
        created_users.append(user)

    # ✅ Create dummy posts if not already many
    existing_posts = Post.objects.count()
    if existing_posts < 8:
        for _ in range(10):
            Post.objects.create(
                user=random.choice(created_users),
                content=random.choice(dummy_posts),
            )

    print("✅ Dummy users + posts created successfully!")
    print("Login credentials:")
    print("Password for all dummy users: 12345678")

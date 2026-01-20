from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("profile/<str:username>/", views.profile_view, name="profile"),

    path("create-post/", views.create_post, name="create_post"),

    path("like/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path("comment/<int:post_id>/", views.add_comment, name="add_comment"),
    path("follow/<str:username>/", views.toggle_follow, name="toggle_follow"),
]

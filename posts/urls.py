from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts_list, name="all"),
    path("posts/<int:post_id>", views.post_detail, name="detail"),
    path("posts/create/", views.add_post, name="create"),
]

from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.posts_list, name="index"),
    path("<int:post_id>", views.post_detail, name="detail"),
]

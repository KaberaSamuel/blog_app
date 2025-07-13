from django.shortcuts import render, get_object_or_404
from .models import Post


def posts_list(request):
    all_posts = Post.objects.all()
    return render(request, "posts.html", {"posts": all_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post.html", {"post": post})

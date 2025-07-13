from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, "home.html")


def posts_list(request):
    all_posts = Post.objects.all()
    return render(request, "posts.html", {"posts": all_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post.html", {"post": post})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/posts/")
    else:
        form = PostForm()

    return render(request, "addpost.html", {"form": form})

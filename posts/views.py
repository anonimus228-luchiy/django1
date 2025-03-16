from django.shortcuts import render
from django.http import HttpResponse
import random
from django.shortcuts import render

from posts.models import Post


def my_view(request):
    return HttpResponse(f"Привет, это текстовый ответ!Номером {random.randint(1,100)}")

def html_view(request):
    return render(request, "test.html")

def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post.html", context={"post": post})

def post_create_view(request):
    return render(request, "post_create.html")


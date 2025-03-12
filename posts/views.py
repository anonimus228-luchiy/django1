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
    return HttpResponse(f"{'. '.join([post.title for post in posts])}")
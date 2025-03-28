from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from posts.models import Post
from users.forms import RegisterForm, LoginForm
from users.models import Profile
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", context={"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "users/register.html", context={"form": form})
        elif form.is_valid():
            form.cleaned_data.__delitem__("password_confirm")
            user = User.objects.create_user(**form.cleaned_data)
            age = form.cleaned_data.pop('age', None)
            image = form.cleaned_data.pop('image', None)
            if not User.objects.filter(username=form.cleaned_data.get("username")).exists():
                form.add_error(None, "User with this username already exists")
                return render(
                    request,
                    "users/register.html",
                    context={"form": form, "error": "User with this username already exists"}
                )
            if user:
                Profile.objects.create(user=user, age=age, image=image)
                return redirect("/")
            else:
                return HttpResponse("error")


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", context={"form": form})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "users/login.html", context={"form": form})
        elif form.is_valid():
            user = authenticate(**form.cleaned_data)
            if not user:
                form.add_error(None, "Invalid username or password")
                return render(request, "users/login.html", context={"form": form})
            elif user:
                login(request, user)
                return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login")
def profile_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "users/profile.html", context={"posts": posts})

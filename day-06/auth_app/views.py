from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, LoginForm, EditProfileForm
from .models import UserProfile


def home(request):
    return render(request, "auth_app/home.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

        context = {"form": form}
        return render(request, "auth_app/signup.html", context)

    form = SignUpForm()
    context = {"form": form}
    return render(request, "auth_app/signup.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")

            context = {
                "form": form,
                "message": "Invalid username or password",
            }
            return render(request, "auth_app/login_user.html", context)

    form = LoginForm()
    context = {"form": form}
    return render(request, "auth_app/login_user.html", context)


@login_required
def logout_user(request):
    logout(request)
    return redirect("home")


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile,
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = EditProfileForm(instance=user_profile)

    context = {
        "form": form,
        "profile": user_profile,
    }

    return render(request, "auth_app/profile.html", context)
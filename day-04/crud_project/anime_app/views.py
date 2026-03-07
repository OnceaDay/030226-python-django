from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime
from .forms import AnimeForm

def home(request):
    if request.method == "POST":
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AnimeForm()

    all_anime = Anime.objects.all()
    return render(request, "anime_app/home.html", {"all_anime": all_anime, "form": form})


def edit_anime(request, id):
    anime_instance = get_object_or_404(Anime, pk=id)

    if request.method == "POST":
        form = AnimeForm(request.POST, instance=anime_instance)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AnimeForm(instance=anime_instance)

    return render(request, "anime_app/edit_anime.html", {"anime": anime_instance, "form": form})


def delete_anime(request, id):
    anime_instance = get_object_or_404(Anime, pk=id)

    if request.method == "POST":
        anime_instance.delete()
        return redirect("home")

    return render(request, "anime_app/delete_anime.html", {"anime": anime_instance})
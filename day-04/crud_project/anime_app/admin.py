from django.contrib import admin
from .models import Anime


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "main_character",
        "year_of_release",
        "runtime",
        "genre",
        "rating"
    )

    search_fields = ("title", "director", "main_character")

    list_filter = ("genre", "rating", "year_of_release")
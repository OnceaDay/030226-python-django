from django import forms
from .models import Anime

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = [
            "title",
            "main_character",
            "runtime",
            "year_of_release",
            "genre",
            "rating",
            "director",
            "writer",
            "cast_star",
            "release_date",
            "gross_revenue",
        ]
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "runtime": forms.NumberInput(attrs={"min": 1}),
            "year_of_release": forms.NumberInput(attrs={"min": 1888}),  # first films era-ish
            "gross_revenue": forms.NumberInput(attrs={"min": 0}),
        }
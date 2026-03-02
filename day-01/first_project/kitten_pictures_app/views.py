from django.shortcuts import render

# HOMEPAGE #
def homepage(request):
    return render(request, "kitten_pictures/homepage.html")
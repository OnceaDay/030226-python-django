from django.urls import path
from . import views

urlpatterns = [
    # when we go to "", show views.homepage
    path("", views.homepage),
    # path("about", views.about),
    # path("profile", views.profile)
]
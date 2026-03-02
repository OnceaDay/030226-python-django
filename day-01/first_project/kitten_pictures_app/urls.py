from django.urls import path
from . import views

urlpatterns = [
    # when we go to "", show views.homepage
    path("", views.homepage, name="homepage"),

    path("about", views.about, name="about"),

    path("gallery", views.gallery, name="gallery"),
                    # parameter will be an int named number
    path("plus-five/<int:number>", views.plus_five, name="plus_five"),
    
    path("gallery/<int:img_index>", views.gallery_detail, name="gallery_detail")
    # name= is helpful for urls and redirects
]
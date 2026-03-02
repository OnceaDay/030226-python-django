from django.shortcuts import render

# HOMEPAGE #
def homepage(request):
    return render(request, "kitten_pictures/homepage.html")

# ABOUT #
def about(request):
    return render(request, "kitten_pictures/about.html")

images_list = [
    "https://www.humaneworld.org/sites/default/files/styles/responsive_3_4_350w/public/2022-07/kitten-playing-575035.jpg.webp?itok=s8zPPwpD",
    
    "https://d2zp5xs5cp8zlg.cloudfront.net/image-61785-800.jpg",
    
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4ZBVltbIEEDTKwVGA2fRX3wW7rT4tR3k_Kw&s",
    
    "https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/kitten-in-top-hat-sarah-kirk.jpg"
]

# GALLERY #
def gallery(request):
    context = {
        "images": images_list,
        "num_images": len( images_list ),
        "current_user": "chett"
    }
    return render(request, "kitten_pictures/gallery.html", context)

# PLUS FIVE #
def plus_five(request, number):
    context = {
        "addition_result": number + 5
    }
    return render(request, "kitten_pictures/plus_five.html", context)

# GALLERY DETAIL #
def gallery_detail(request, img_index):
    # try means we're going TRY to do something
    # ... but it might error out
    try:
        # find kitten 
        img_url = images_list[img_index]
        context = {
            "img_url": img_url
        }
        return render(request, "kitten_pictures/gallery_detail.html", context)
    # if it does error out with an IndexError
    # ... show a different page, in this case a 404 page
    except IndexError:
        return render(request, "kitten_pictures/four_oh_four.html")
from django.db import models

class Anime(models.Model):

    # GENRE_CHOICES = [
    #     ("action", "Action"),
    #     ("blaxploitation", "Blaxploitation"),
    #     ("comedy", "Comedy"),
    #     ("drama", "Drama"),
    #     ("sci_fi", "Sci-Fi"),
    #     ("thriller", "Thriller"),
    #     ("horror", "Horror"),
    #     ("romance", "Romance"),
    #     ("fantasy", "Fantasy"),
    #     ("animation", "Animation"),
    #     ("documentary", "Documentary"),
    # ]


    GENRE_CHOICES = [
        ("action", "Action"),
        ("animation", "Animation"),
        ("blaxploitation", "Blaxploitation"),
        ("comedy", "Comedy"),
        ("documentary", "Documentary"),
        ("drama", "Drama"),
        ("fantasy", "Fantasy"),
        ("horror", "Horror"),
        ("romance", "Romance"),
        ("sci_fi", "Sci-Fi"),
        ("thriller", "Thriller"),
        
    ]






    RATING_CHOICES = [
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
        ("NR", "Not Rated"),
    ]

    title = models.CharField(max_length=255)
    main_character = models.CharField(max_length=255)
    runtime = models.IntegerField()
    year_of_release = models.IntegerField()

    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES
    )

    rating = models.CharField(
        max_length=10,
        choices=RATING_CHOICES,
        null=True,
        blank=True
    )

    # optional fields
    director = models.CharField(max_length=255, null=True, blank=True)
    writer = models.CharField(max_length=255, null=True, blank=True)
    cast_star = models.CharField(max_length=500, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    gross_revenue = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
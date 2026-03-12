from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    BUDGET_TIERS = [
        ("budget", "Budget"),
        ("midrange", "Midrange"),
        ("premium", "Premium"),
    ]

    SPACE_REQUIREMENTS = [
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=275, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    short_description = models.CharField(max_length=255, blank=True)
    long_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    budget_tier = models.CharField(max_length=20, choices=BUDGET_TIERS, blank=True)
    space_requirement = models.CharField(max_length=20, choices=SPACE_REQUIREMENTS, blank=True)

    in_stock = models.BooleanField(default=True)
    quantity_available = models.PositiveIntegerField(default=0)

    tags = models.JSONField(default=list, blank=True)
    features = models.JSONField(default=list, blank=True)
    accessibility_features = models.JSONField(default=list, blank=True)

    primary_image = models.URLField(blank=True)
    gallery_images = models.JSONField(default=list, blank=True)
    image_alt_text = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
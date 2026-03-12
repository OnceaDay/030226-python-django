from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


class UserProfile(models.Model):
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=200)
    profile_photo = models.ImageField(null=True, blank=True, upload_to="profile_photos")

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_profile = UserProfile(user=instance)
        new_profile.save()
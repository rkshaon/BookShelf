from django.db.models.signals import post_delete
from django.dispatch import receiver

from user_api.models import User


@receiver(post_delete, sender=User)
def user_delete(sender, instance, **kwargs):
    """
    Deletes the profile image of the user
    when the user is deleted.
    """
    if instance.profile_image:
        instance.profile_image.delete(save=False)

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomUser

@receiver(models.signals.post_delete, sender=CustomUser)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image.url != 'default.jpg':
        instance.image.delete(save=False)


@receiver(models.signals.pre_save, sender=CustomUser)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_image = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_image = instance.image.path
        except Exception:
            new_image = None
        if new_image != old_image:
            import os
            if os.path.exists(old_image):
                if 'default.jpg' not in os.path.exists(old_image):
                    os.remove(old_image)
    except Exception:
        pass
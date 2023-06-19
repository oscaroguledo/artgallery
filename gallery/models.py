from django.db import models
from account.models import CustomUser

# Create your models here.

class Art(models.Model):
    name = models.CharField(verbose_name="Name of the work", max_length=100)
    type = models.CharField(verbose_name="Type of the work", max_length=100)
    art_by = models.CharField(verbose_name="Owner of the art", max_length=100)
    uploaded_by = models.ForeignKey(CustomUser, verbose_name="User name", on_delete=models.CASCADE)
    date_uploaded = models.CharField(verbose_name="Date uploaded", max_length=100)

class Attachment(models.Model):
    name = models.CharField(verbose_name="Name of the work", max_length=100)
    image = models.CharField(verbose_name="Image of the work", max_length=100)
    art = models.ForeignKey(Art, verbose_name="Art", on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(CustomUser, verbose_name="User name", on_delete=models.CASCADE)
    date_added = models.CharField(verbose_name="Date Added", max_length=100)
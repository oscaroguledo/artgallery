from django.db import models
from account.models import CustomUser

# Create your models here.

class Art(models.Model):
    name = models.CharField(verbose_name="Name of the work", max_length=100)
    type = models.CharField(verbose_name="Type of the work", max_length=100)
    image = models.ImageField(verbose_name="Image of the work", max_length=100, default="default.jpg")
    art_by = models.CharField(verbose_name="Owner of the art", max_length=100)
    uploaded_by = models.ForeignKey(CustomUser, verbose_name="Uploaded By", on_delete=models.CASCADE)
    date_uploaded = models.DateField(verbose_name="Date Uploaded",auto_now_add=True)

    def __str__(self):
        return f"{self.name}  by {self.art_by}"

class Attachment(models.Model):
    name = models.CharField(verbose_name="Name of the work", max_length=100)
    image = models.ImageField(verbose_name="Image of the work", max_length=100)
    art = models.ForeignKey(Art, verbose_name="Art", on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(CustomUser, verbose_name="Uploaded By", on_delete=models.CASCADE)
    date_added = models.DateField(verbose_name="Date Added",auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
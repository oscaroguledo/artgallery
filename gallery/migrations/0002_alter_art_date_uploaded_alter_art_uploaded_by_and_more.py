# Generated by Django 4.1.5 on 2023-06-19 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True, verbose_name='Date Uploaded'),
        ),
        migrations.AlterField(
            model_name='art',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Uploaded By'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='date_added',
            field=models.DateField(auto_now_add=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Uploaded By'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-06-19 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of the work')),
                ('type', models.CharField(max_length=100, verbose_name='Type of the work')),
                ('art_by', models.CharField(max_length=100, verbose_name='Owner of the art')),
                ('date_uploaded', models.CharField(max_length=100, verbose_name='Date uploaded')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User name')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of the work')),
                ('image', models.CharField(max_length=100, verbose_name='Image of the work')),
                ('date_added', models.CharField(max_length=100, verbose_name='Date Added')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.art', verbose_name='Art')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User name')),
            ],
        ),
    ]

from django.db import models

# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to="gallery")

class Video(models.Model):
    vid = models.FileField(upload_to="videos")
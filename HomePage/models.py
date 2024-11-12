from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
import os

# Create your models here.

class Projects(models.Model):
    topic = models.CharField(max_length=50, unique=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="images/Homepage")

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and os.path.exists(self.image.path):
            img = Image.open(self.image.path)

            output_size = (720, 1080)
            img.thumbnail(output_size)

            webp_path = os.path.splitext(self.image.path)[0] + '.webp'
            img.save(webp_path, 'webp', optimize=True, quality=90)

            self.image.name = os.path.splitext(self.image.name)[0] + '.webp'
            super().save(*args, **kwargs)


class ClubActivity(models.Model):
    activity = models.CharField(max_length=50, unique=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="Homepage/ClubActivity")

    def __str__(self):
        return self.activity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and os.path.exists(self.image.path):
            img = Image.open(self.image.path)

            output_size = (720, 1080)
            img.thumbnail(output_size)

            webp_path = os.path.splitext(self.image.path)[0] + '.webp'
            img.save(webp_path, 'webp', optimize=True, quality=90)

            self.image.name = os.path.splitext(self.image.name)[0] + '.webp'
            super().save(*args, **kwargs)

class Achievements(models.Model):
    achievement = models.CharField(max_length=150, unique=True)
    link = models.CharField(max_length=150, default="#")

    def __str__(self):
        return self.achievement


class Fests(models.Model):
    festname = models.CharField(max_length=50, unique=True)
    description = RichTextField(blank=True, null=True)
    link = models.CharField(max_length=150, default="#/")
    image = models.ImageField(default="default.jpg", upload_to="Homepage/Fests")

    def __str__(self):
        return self.festname

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and os.path.exists(self.image.path):
            img = Image.open(self.image.path)

            output_size = (720, 1080)
            img.thumbnail(output_size)

            webp_path = os.path.splitext(self.image.path)[0] + '.webp'
            img.save(webp_path, 'webp', optimize=True, quality=90)

            self.image.name = os.path.splitext(self.image.name)[0] + '.webp'
            super().save(*args, **kwargs)
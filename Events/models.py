from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
import os

class Astrax(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="images/Astrax")
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

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


class Pleiades(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="images/Pleiades")
    description = RichTextField(blank=True, null=True)
    problem_statement = models.URLField(default="", blank=True, null=False)

    def __str__(self):
        return self.name

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

class Zenith(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="images/Zenith")
    description = RichTextField(blank=True, null=True)
    problem_statement = models.URLField(default="", blank=True, null=False)

    def __str__(self):
        return self.name

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

class Utkarsh(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="images/Utkarsh")
    description = RichTextField(blank=True, null=True)
    problem_statement = models.URLField(default="", blank=True, null=False)

    def __str__(self):
        return self.name

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


from django.db import models
from PIL import Image


class core_team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    fb = models.CharField(max_length=50, default="#")
    insta = models.CharField(max_length=50, default="#")
    git = models.CharField(max_length=50, default="#")
    linkedin = models.CharField(max_length=50, default="#")
    batch = models.IntegerField(default=2023)  # positioning batch wise
    image = models.ImageField(
        default="default.jpg", upload_to="team/core_team"
    )

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class coordinators(models.Model):
    name = models.CharField(max_length=50, unique=True)
    fb = models.CharField(max_length=50, default="#")
    insta = models.CharField(max_length=50, default="#")
    git = models.CharField(max_length=50, default="#")
    linkedin = models.CharField(max_length=50, default="#")
    batch = models.IntegerField(default=2023)
    image = models.ImageField(
        default="default.jpg", upload_to="team/coordinators"
    )

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

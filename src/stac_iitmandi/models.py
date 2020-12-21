from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField


class core_team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    fb = models.CharField(max_length=50, default="#")
    insta = models.CharField(max_length=50, default="#")
    git = models.CharField(max_length=50, default="#")
    linkedin = models.CharField(max_length=50, default="#")
    batch = models.IntegerField(default=2023)  # positioning batch wise
    image = models.ImageField(default="default.jpg", upload_to="team/core_team")

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 240 or img.width > 240:
            output_size = (240, 240)
            img.thumbnail(output_size)
            img.save(self.image.path)


class coordinators(models.Model):
    name = models.CharField(max_length=50, unique=True)
    fb = models.CharField(max_length=50, default="#")
    insta = models.CharField(max_length=50, default="#")
    git = models.CharField(max_length=50, default="#")
    linkedin = models.CharField(max_length=50, default="#")
    batch = models.IntegerField(default=2023)
    image = models.ImageField(default="default.jpg", upload_to="team/coordinators")

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 240 or img.width > 240:
            output_size = (240, 240)
            img.thumbnail(output_size)
            img.save(self.image.path)


#####  For Homepage ######
class club_activity(models.Model):
    activity = models.CharField(max_length=50, unique=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="Homepage/club_activity")

    def __str__(self):
        return self.activity

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 1280 or img.width > 720:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)


# future projects, competetions and events_intro on homepage in one table #
class homepage(models.Model):
    topic = models.CharField(max_length=50, unique=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="Homepage")

    def __str__(self):
        return self.topic

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 1280 or img.width > 720:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)

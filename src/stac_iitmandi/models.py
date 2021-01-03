from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField


class core_team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    fb = models.URLField(default="", blank=True, null=False)
    insta = models.URLField(default="", blank=True, null=False)
    git = models.URLField(default="", blank=True, null=False)
    linkedin = models.URLField(default="", blank=True, null=False)
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
    fb = models.URLField(default="", blank=True, null=False)
    insta = models.URLField(default="", blank=True, null=False)
    git = models.URLField(default="", blank=True, null=False)
    linkedin = models.URLField(default="", blank=True, null=False)
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


# For Homepage
class club_activity(models.Model):
    activity = models.CharField(max_length=50, unique=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="Homepage/club_activity")

    def __str__(self):
        return self.activity

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 720 or img.width > 1080:
            output_size = (720, 1080)
            img.thumbnail(output_size)
            img.save(self.image.path)


# Zenith
class zenithEvents(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="Zenith/event_image")
    description = RichTextField(blank=True, null=True)
    problem_statement = models.URLField(default="", blank=True, null=False)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (720, 1080)
        img.thumbnail(output_size)
        img.save(self.image.path)


# Utkarsh
class utkarshEvents(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="Utkarsh/event_image")
    description = RichTextField(blank=True, null=True)
    problem_statement = models.URLField(default="", blank=True, null=False)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (720, 1080)
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
        if img.height > 720 or img.width > 1080:
            output_size = (720, 1080)
            img.thumbnail(output_size)
            img.save(self.image.path)


# Achievements #
class achievements(models.Model):
    achievement = models.CharField(max_length=150, unique=True)
    link = models.CharField(max_length=150, default="#")

    def __str__(self):
        return self.achievement


# Astrax
class Astrax(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="Astrax")
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (720, 1080)
        img.thumbnail(output_size)
        img.save(self.image.path)


# Pleiades
class Pleiades(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="Pleiades")
    description = RichTextField(blank=True, null=True)
    problem_statement = models.URLField(default="", blank=True, null=False)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (720, 1080)
        img.thumbnail(output_size)
        img.save(self.image.path)


# about
class About(models.Model):
    content = models.CharField(default="", max_length=50, unique=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="About")

    def __str__(self):
        return self.content

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (720, 1080)
        img.thumbnail(output_size)
        img.save(self.image.path)


# photogallery
class photogallery(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    image = models.ImageField(default="default.jpg", upload_to="Gallery/Photogallery")
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (720, 1080)
        img.thumbnail(output_size)
        img.save(self.image.path)


# videogallery
class videogallery(models.Model):
    videoname = models.CharField(default="", max_length=50, unique=True)
    link = models.URLField(default="#/", blank=True, null=False)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.videoname


# Alumni
class Alumni(models.Model):
    name = models.CharField(default="", max_length=50, unique=True)
    description = RichTextField(blank=True, null=True)
    fb = models.URLField(default="#/", blank=True, null=False)
    insta = models.URLField(default="#/", blank=True, null=False)
    git = models.URLField(default="#/", blank=True, null=False)
    linkedin = models.URLField(default="#/", blank=True, null=False)
    image = models.ImageField(default="default.jpg", upload_to="Alumni")

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (720, 1080)
        img.thumbnail(output_size)
        img.save(self.image.path)


# Links to website#
class Links(models.Model):
    linkname = models.CharField(max_length=50, unique=True)
    link = models.CharField(max_length=150, default="#/")

    def __str__(self):
        return self.linkname

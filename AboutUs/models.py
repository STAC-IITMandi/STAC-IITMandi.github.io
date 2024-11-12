from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField 
import os

class aboutUs(models.Model):
    content = models.CharField(max_length=50, unique=True, default="")
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(default="default.webp", upload_to="images/AboutUs")

    def __str__(self):
        return self.content

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



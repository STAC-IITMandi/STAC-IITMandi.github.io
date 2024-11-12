from django.db import models
from PIL import Image
import os

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='email')
    message = models.CharField(max_length=100, default='andhera_kayam_rahe')

    linkedin_url  = models.CharField(max_length=100, default='linkedin')
    instagram_url = models.CharField(max_length=100, default='instagram')
    image = models.ImageField(default="default.webp", upload_to="images/CoreTeam")

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

from django.db import models
from PIL import Image
import os

class MemberDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)

    POSITIONS = (
        ('A', 'Coordinator'),  
        ('B', 'Co-coordinator'),
        ('C', 'Core Team'),
        ('D', 'Mentor'),
    )

    position = models.CharField(max_length=1, choices=POSITIONS, default='C')

    linkedin_url  = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
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

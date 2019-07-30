from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


# Create your models here.
class Printer(models.Model):
    name = models.CharField(max_length=50, help_text='Name of your printer')
    owner = models.CharField(max_length=50, help_text='Name of the owner')
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=500, help_text="Where is your printer located? Street, building, floor, Shop Number")
    opening_hours = models.TimeField(auto_now_add=True, help_text="The time your shop opens eg 8.00 a.m.")
    closing_hours = models.TimeField(auto_now_add=True, help_text="The time your shop closes eg 5.00 p.m.")
    delivery = models.CharField(max_length=3, default="YES", help_text="Do you offer delivery services(Yes/No)")
    phone = models.IntegerField(help_text="Your working phone number")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('printer-home')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

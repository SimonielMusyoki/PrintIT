from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class PrintItem(models.Model):
    upload = models.FileField(upload_to='uploads/')
    pages = models.IntegerField(help_text="Number of pages in the document")
    copies = models.IntegerField(default=1, help_text="Number of copies to be printed. e.g 2")
    printer = models.CharField(max_length=200, help_text="Where do you want the copy to be printed")
    time = models.TimeField(auto_now_add=True)
    owner = models.CharField(max_length=200,default='',blank=True)

    def __str__(self):
        return self.upload.name

    def get_absolute_url(self):
        return reverse('home')




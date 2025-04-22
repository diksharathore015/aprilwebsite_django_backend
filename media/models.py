from django.db import models
from courses.models import *
# Create your models here.
 

class Media(models.Model): 
     
    alternative_test = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    caption = models.CharField( max_length=250,  blank=True, null=True , default="captions")
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='media/')
    size = models.PositiveIntegerField(blank=True, null=True)  # Size in bytes
    url = models.URLField(blank=True, null=True)
    course = models.ManyToManyField(Course,   related_name='media', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        # Update file size upon saving
        if self.file:
            self.size = self.file.size
        super().save(*args, **kwargs)

class Media_video(models.Model): 
     
    alternative_test = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    caption = models.CharField( max_length=250,  blank=True, null=True , default="captions")
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='video/')
    size = models.PositiveIntegerField(blank=True, null=True)  # Size in bytes
    url = models.URLField(blank=True, null=True)
    course = models.ManyToManyField(Course,   related_name='media_video', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        # Update file size upon saving
        if self.file:
            self.size = self.file.size
        super().save(*args, **kwargs)
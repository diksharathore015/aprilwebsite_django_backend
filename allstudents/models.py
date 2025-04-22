from django.db import models

# from courses.models import Course'

from django.utils.text import slugify
from location.models import *
from media.models import Media 
class Student(models.Model):
    name = models.CharField(max_length=255 , blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True , )
    homepage = models.BooleanField(default=False , blank=True, null=True)
    detail = models.CharField(max_length=500, blank=True, null=True)
    meta_title = models.CharField(max_length=500, blank=True, null=True)
    meta_descriptions = models.CharField(max_length=1000, blank=True, null=True)
    meta_keyWords = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ManyToManyField(Media,  null=True, blank=True, related_name="allstudentsmedia")
    courses = models.ManyToManyField('courses.Course', related_name='allstudentslist' , null=True, blank=True)
    states = models.ManyToManyField(State, related_name='allstudents' , null=True, blank=True)
    cities = models.ManyToManyField(City, related_name='allstudents' , null=True, blank=True)
    localities = models.ManyToManyField(Locality, related_name='allstudents' , null=True, blank=True)
    contact_number = models.CharField(max_length=1500, blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    rating = models.CharField(max_length=500, blank=True, null=True)
    review = models.CharField(max_length=500, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Student, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

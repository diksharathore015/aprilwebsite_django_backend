from django.db import models
from location.models import *
# from allstudents.models import Student

from django.utils.text import slugify
class Course(models.Model):
    title = models.CharField(max_length=5550)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slider_images = models.JSONField(default=list, blank=True)
    meta_title = models.CharField(max_length=1000, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=1000, blank=True, null=True)
    contact_number = models.CharField(max_length=1000, blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    state = models.ManyToManyField(State, related_name='state') 
    city = models.ManyToManyField(City, related_name='city') 
    locality = models.ManyToManyField(Locality, related_name='locality') 
    student_list =  models.ManyToManyField('allstudents.Student', related_name='stidentlists' , blank=True, null=True) 
    created_by =  models.CharField(max_length=5550 ,blank=True, null=True)
    price =  models.CharField(max_length=5550 ,blank=True, null=True)
    duration =models.CharField(max_length=550 ,blank=True, null=True ,default="3months")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    

class Instructor(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()  # in years
    contact_number = models.CharField(max_length=25, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="instructor_profiles/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name="instructors" , null=True, blank=True)  # Many-to-Many Relationship
    def __str__(self):
        return self.name
    

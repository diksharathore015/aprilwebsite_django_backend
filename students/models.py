from django.db import models
from media.models import *
# Create your models here.
from courses.models import *
# class Student(models.Model):
#     name = models.CharField(max_length=255)
   
#     def __str__(self):
#         return self.name

class Students(models.Model):
    name = models.CharField(max_length=255)
    detail =  models.CharField(max_length=500 ,blank=True, null=True) 
    meta_title =  models.CharField(max_length=500,blank=True, null=True) 
    meta_descriptions =  models.CharField(max_length=1000 ,blank=True, null=True) 
    meta_keyWords =    models.CharField(max_length=1000 ,blank=True, null=True) 
    #  image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, related_name="students")
    image = models.ManyToManyField(Media, related_name="students_images", blank=True)
    
    course= models.ManyToManyField(Course, related_name='students'  )
    state = models.ManyToManyField(State, related_name='students', blank=True, null=True)
    city = models.ManyToManyField(City, related_name='students', blank=True, null=True)
    localities = models.ManyToManyField(Locality, related_name='students', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    rating  =models.CharField(max_length=500 ,blank=True, null=True)  
    review  =  models.CharField(max_length=500 ,blank=True, null=True) 
    def __str__(self):
        return self.name

# class Student(models.Model):
#     name = models.CharField(max_length=255)
#     detail =  models.CharField(max_length=500 ,blank=True, null=True) 
#     meta_title =  models.CharField(max_length=500,blank=True, null=True) 
#     meta_descriptions =  models.CharField(max_length=1000 ,blank=True, null=True) 
#     meta_keyWords =    models.CharField(max_length=1000 ,blank=True, null=True) 
#     #  image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, related_name="students")
#     image = models.ManyToManyField(Media, related_name="students_images", blank=True)
    
#     courses = models.ManyToManyField(Course, related_name='students' ,blank=True, null=True)
#     states = models.ManyToManyField(State, related_name='students', blank=True, null=True)
#     cities = models.ManyToManyField(City, related_name='students', blank=True, null=True)
#     localities = models.ManyToManyField(Locality, related_name='students', blank=True, null=True)
#     contact_number = models.CharField(max_length=15, blank=True, null=True)
#     youtube_link = models.URLField(blank=True, null=True)
#     facebook_link = models.URLField(blank=True, null=True)
#     instagram_link = models.URLField(blank=True, null=True)
#     rating  =models.CharField(max_length=500 ,blank=True, null=True)  
#     review  =  models.CharField(max_length=500 ,blank=True, null=True) 
#     def __str__(self):
#         return self.name

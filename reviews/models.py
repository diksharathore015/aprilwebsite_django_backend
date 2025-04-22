from django.db import models

from .models import * 
from allstudents.models import * 
from courses.models import * 

# Create your models here.
class Review(models.Model):
    student = models.ManyToManyField(Student, related_name='reviews' )
    course = models.ManyToManyField(Course, related_name='reviews')  # Corrected related_name
    title = models.CharField(max_length=500)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Review - {self.title}"

from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255 ,null=True, blank=True )
    image = models.ImageField(upload_to='state_images/', null=True, blank=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    lat  = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)
    pincode= models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.state_name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    city_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255 , null=True, blank=True)
    image = models.ImageField(upload_to='city_images/', null=True, blank=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True )
    instagram = models.URLField(null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    lat  = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)
    pincode= models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.city_name


class Locality(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='localities' ,null=True, blank=True)
    locality_name = models.CharField(max_length=255 ,null=True, blank=True)
    title = models.CharField(max_length=255 , null=True, blank=True)
    image = models.ImageField(upload_to='locality_images/', null=True, blank=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    lat  = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)
    pincode= models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.locality_name

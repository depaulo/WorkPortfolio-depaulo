from django.db import models

# Create your models here.
class Job(models.Model):    
    image = models.ImageField(upload_to='images/') #images, are upload here 
    summary = models.CharField(max_length=200) #summary

    def __str__(self):# this is necessary to show the description on the admin module
        return self.summary
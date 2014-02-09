from django.db import models

class Listing(models.Model):
    def __unicode__(self):
       return self.title;

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    skillsNeeded = models.CharField(max_length=200)
    dateAdded = models.DateTimeField('date published')
    email = models.EmailField(max_length=75)
    image = models.ImageField(upload_to="images/", max_length=75, null=True, blank=True)
    video = models.URLField(max_length=200, null=True, blank=True)
   

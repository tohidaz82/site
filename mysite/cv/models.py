from django.db import models
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('information', kwargs={'pk': self.pk})
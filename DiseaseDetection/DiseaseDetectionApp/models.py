from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Malaria(models.Model):
    malaria_img = models.ImageField(upload_to='images/')
    prediction = models.CharField(max_length=50)

class Cancer(models.Model):
    cancer_img = models.ImageField(upload_to='images/')
    prediction = models.CharField(max_length=50)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)

    # portfolio_site = models.URLField(blank=True)

    # profile_pic = models.ImageField(upload_to='profile_pic', blank=True)


    def __str__(self):
        return self.user.username

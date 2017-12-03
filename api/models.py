from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

# This code is triggered whenever a new user has been created and saved to the database



class profiledetails(models.Model):
    profile_image = models.ImageField(upload_to='profilepics/%Y/%m/%d/', null=True, max_length=255)
    user = models.ForeignKey(User, related_name='user_profile')
    gender = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    short_bio = models.TextField(null=True)


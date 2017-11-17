from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

# This code is triggered whenever a new user has been created and saved to the database

class posts(models.Model):
    title = models.CharField(max_length=255,)
    content = models.TextField()
    user = models.OneToOneField(User,null=True)

class userposts(models.Model):
    title = models.CharField(max_length=244)
    post = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,primary_key=True)


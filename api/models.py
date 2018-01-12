from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager




# This code is triggered whenever a new user has been created and saved to the database



class profiledetails(models.Model):
    profile_image = models.ImageField(upload_to='profilepics/%Y/%m/%d/', null=True, max_length=255)
    user = models.OneToOneField(User, related_name='user_profile')
    gender = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    short_bio = models.TextField(null=True)
    followers = models.ManyToManyField('profiledetails',related_name="followers_profile", blank=True)
    following = models.ManyToManyField('profiledetails',related_name='following_profile',blank=True)
    type = models.CharField(max_length=20,null=True)
    follow_id = models.IntegerField(max_length=20,null=True)




class post(models.Model):
    user = models.ForeignKey(User,related_name='user_posts')
    caption = models.TextField(max_length=255)
    post_pic = models.ImageField(upload_to='postimages/%Y/%m/%d/', null=True, max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True,null=True)









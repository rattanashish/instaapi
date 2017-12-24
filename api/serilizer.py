from rest_framework import serializers
from django.contrib.auth.models import User # If used custom user model
from .models import *

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name =validated_data['first_name'],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')




class profileserlizer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.first_name')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = profiledetails
        fields = ('profile_image','id','name','email','gender')

class postserlizer(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = ('caption','post_pic',)


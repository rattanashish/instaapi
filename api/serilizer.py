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
        fields = ('username','email','password','first_name','last_name','id')




class profileserlizer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.first_name')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = profiledetails
        fields = ('profile_image','id','name','email','gender','short_bio','pk')

class postserlizer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = post
        fields = ('caption','post_pic','id','name','user_id')

class followfollowingserlizer(serializers.ModelSerializer):

    class Meta:
        model = profiledetails
        fields = ('type','follow_id',)

class profileupdateserlizer(serializers.ModelSerializer):
    class Meta:
        model = profiledetails
        fields = '__all__'


class user_bac_serilzer(serializers.ModelSerializer):

    class Meta:
        model = user_bac
        fields = ('user_video','timestamp',)
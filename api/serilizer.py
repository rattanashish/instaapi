from rest_framework import serializers
from django.contrib.auth.models import User # If used custom user model
from .models import posts,userposts



User = User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name =validated_data['first_name']


        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['username','email','password','first_name']
class postserlizer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')



    class Meta:
        model = posts
        fields = '__all__'

class userpostserilizer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.username')

   class Meta:
       model = userposts
       fields = '__all__'




import token

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from  rest_framework.response import Response
from  rest_framework import status
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .serilizer import *
from rest_framework.views import APIView
from .models import *
from .models import profiledetails as modelprofile
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import profiledetails as prodet

from rest_framework.parsers import MultiPartParser,FileUploadParser
from django.shortcuts import get_object_or_404



class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})



class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class profiledetails(APIView):
    parser_classes = (MultiPartParser,FileUploadParser)

    def get(self, request, format=None):
        snippets = prodet.objects.filter(user = self.request.user)
        serializer = profileserlizer(snippets, many=True)
        pro_post = serializer.data
        numb = post.objects.filter(user = self.request.user)
        number_of_posts = numb.count()
        post_objects = post.objects.filter(user=self.request.user)
        abc = postserlizer(post_objects, many=True)
        post_in_profile = abc.data

        return Response({'profiledetails': pro_post,'number_of_posts':number_of_posts,'posts':post_in_profile})

    def post(self, request, format=None):
        serializer = profileserlizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            pro_post = serializer.data
            filter_of_posts = post.objects.filter(user = self.request.user)
            number_of_posts = filter_of_posts.count()

            post_pro_d = post.objects.filter(user = self.request.user)
            post_pro_serlizer = postserlizer(post_pro_d,many=True)
            post_pro_details = post_pro_serlizer.data

            return Response({'profiledetails':pro_post,'number_of_posts':number_of_posts,'posts':post_pro_details})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class postview(APIView):

    def get(self, request, format=None):
        snippets = post.objects.filter(user = self.request.user)
        serializer = postserlizer(snippets, many=True)


        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = postserlizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class followfollowingview(APIView):
    def post(self,request):
        serializer = followfollowingserlizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
        testser = serializer.data

        user_profile = prodet.objects.filter(user=request.user) 
        follow_id = testser['follow_id']
        follow_profile = prodet.objects.filter(user_id=follow_id)
        if testser['type']=='follow':
            user_profile.following.add(follow_profile)
            follow_profile.followers.add(user_profile)
        elif testser['type']=='unfollow':
            user_profile.following.remove(follow_profile)
            follow_profile.followers.remove(user_profile)
        return Response(testser)


class profiledetailsupdate(APIView):
    def post(self,request):
        serializer = profileserlizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user= self.request.user)
        return Response(serializer.data)


class exp(APIView):
    def post(self,request):
        serializer = postserlizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        return Response(serializer.data)

    def get(self,request):
        serializer = post.objects.filter(user_ = 'ashu')
        dat = postserlizer(serializer,many=True)
        return Response(dat.data)

class user_bac_view(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
                          ]

    def post(self,request):
        serializer = user_bac_serilzer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        ser = user_bac.objects.filter(user = self.request.user)
        serializer = user_bac_serilzer(ser,many=True)

        return Response(serializer.data)

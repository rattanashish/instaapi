from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from  rest_framework.response import Response
from  rest_framework import status
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework import authentication
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .serilizer import UserSerializer,postserlizer,userpostserilizer
from rest_framework.views import APIView
from .models import posts
from .models import userposts as usepostsModel
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


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
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

class listusers(APIView):

    def post(self,request):
        serilizer = postserlizer(data=request.data)
        if serilizer.is_valid():
            user = serilizer.save()
            return Response(user,status=status.HTTP_201_CREATED)
    def perform_create(self,serilizer):
        serilizer.save(owner=self.request.user)


    def get(self, request, format=None):
        postsas = posts.objects.all().filter(user= self.request.user)
        serializer =postserlizer(postsas, many=True)
        return Response(serializer.data)


class userposts(APIView):
    def post(self, request):
        serilizer = userpostserilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serlilizer):
        serlilizer.save(owner=self.request.user)


    def get(self,request):
        postsa = usepostsModel.objects.all().filter(owner = self.request.user)
        serlizer = userpostserilizer(postsa,many=True)
        return Response(serlizer.data)






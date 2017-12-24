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
                return Response({'Reg':json})

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

    def get(self, request, format=None):
        snippets = prodet.objects.all()
        serializer = profileserlizer(snippets, many=True)
        pro_post = serializer.data
        numb = post.objects.count()

        return Response({'profiledetails': pro_post,'number_of_posts':numb})

    def post(self, request, format=None):
        serializer = profileserlizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            pro_post = serializer.data
            number_of_posts = post.objects.count()

            return Response({'profiledetails':pro_post,'number_of_posts':number_of_posts})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class postview(APIView):

    def get(self, request, format=None):
        snippets = post.objects.all()
        serializer = postserlizer(snippets, many=True)

        return Response({'postdetails': serializer.data})


    def post(self, request, format=None):
        serializer = postserlizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response({'postdetails': serializer.data} )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



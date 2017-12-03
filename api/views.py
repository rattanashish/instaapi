import token

# Create your views here.
from rest_framework.generics import ListCreateAPIView
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



class profiledetails(ListCreateAPIView):
    model = profiledetails
    serializer_class = profileserlizer
    queryset = profiledetails.objects.all()

    def get_queryset(self):
        return modelprofile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




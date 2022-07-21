from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

# Create your views here.


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

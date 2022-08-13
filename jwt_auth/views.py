from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

# Create your views here.


class MyObtainTokenPairView(TokenObtainPairView):
    """
    GET: Takes a set of user credentials and returns an access and refresh JSON web
         token pair to prove the authentication of those credentials.
    Uses custom serializer - jwt_auth.serializers.MyTokenObtainPairSerializer
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    POST: creates new model.User entity
    Uses custom serializer - jwt_auth.serializers.RegisterSerializer
    """
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

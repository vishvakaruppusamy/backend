from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()


# --- Register View ---
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]  # Accept JSON + Form input

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.to_representation(user), status=status.HTTP_201_CREATED)


# --- Login View (with browsable API form) ---
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]  # Accept JSON + Form input

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data  # authenticated user object
        return Response(serializer.to_representation(user), status=status.HTTP_200_OK)


# --- User Profile View ---
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

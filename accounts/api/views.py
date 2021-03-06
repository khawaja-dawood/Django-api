from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .serializer import UserRegisterSerializer
from accounts.api.user.serializers import UserDetailSerializer

from accounts.api.permissions import AnonPermissionOnly, IsOwnerOrReadOnly

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class AuthAPIView(APIView):
    # api endpoint for data get without signing in, anyone can access this authenticated or unauthenticated users
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username')  # username or email address
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct()
        print(data)
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    # registering a user using useranme, email ,password and password2
    queryset = User.objects.all()
    permission_classes = [AnonPermissionOnly]
    serializer_class = UserRegisterSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}






# class RegisterAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return Response({'detail': 'You already registered and authenticated'}, status=400)
#         data = request.data
#         username = data.get('username')
#         email = data.get('email')  # username or email address
#         password = data.get('password')
#         password2 = data.get('password2')
#         qs = User.objects.filter(
#             Q(username__iexact=username) |
#             Q(email__iexact=username)
#         ).distinct()
#         if password != password2:
#             return Response({'detail': 'Both passwords must match'}, status=401)
#         if qs.exists():
#             return Response({'detail': 'This user already exists'}, status=401)
#         else:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(token, user, request=request)
#             return Response(response, status=201)
#         # return Response({"detail": "Invalid credentials"}, status=400)

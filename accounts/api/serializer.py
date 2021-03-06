from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
import datetime


jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta                    = api_settings.JWT_REFRESH_EXPIRATION_DELTA

user = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = user
        fields = ['id', 'username', 'uri']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={'username': obj.username}, request=request)
        # return api_reverse("<namespace>:<url_name or view_name>", kwargs={'username': obj.username})
        # return f"http://127.0.0.1:8000/api/users/{obj.username}/"


class UserRegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)
    # token_response = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = user
        fields = ['username', 'email', 'password', 'password2', 'token', 'expires', 'message']
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self):
        return 'Thank you for registering your account'

    def validate_username(self, value):
        qs = user.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this username already exists!')
        return value

    def validate_email(self, value):
        qs = user.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this email already exists!')
        return value

    def get_token(self, obj):
        _user = obj
        payload = jwt_payload_handler(_user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    # get_token_response
    # def get_token_response(self, obj):
    #     payload = jwt_payload_handler(obj)
    #     token = jwt_encode_handler(payload)
    #     context = self.context
    #     request = context['request']
    #     print(request.user.is_authenticated)
    #     response = jwt_response_payload_handler(token, user, request=context['request'])
    #     return response

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')

        if pw != pw2:
            raise serializers.ValidationError("Passwords must match!")
        return data

    def create(self, validated_data):
        print(validated_data)
        user_obj = user(username=validated_data.get('username'), email=validated_data.get('email'))
        user_obj.set_password = validated_data.get('password')
        user_obj.save()
        return user_obj
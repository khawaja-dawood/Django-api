from rest_framework import serializers
from .models import Post
from accounts.api.serializer import UserPublicSerializer


class PostInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['uri', 'id', 'title', 'description', 'image', 'file']

    def get_uri(self, obj):
        return f"http://127.0.0.1:8000/api/post/{obj.id}/"

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


class PostSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['uri', 'id', 'title', 'description', 'owner', 'image', 'file']
        read_only_fields = ['owner']

    def get_uri(self, obj):
        return f"http://127.0.0.1:8000/api/post/{obj.id}/"

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data

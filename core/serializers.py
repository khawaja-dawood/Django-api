from rest_framework import serializers
from .models import Post, Book, Review
from accounts.api.serializer import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse


class PostInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['uri', 'id', 'title', 'description', 'image', 'file']

    def get_uri(self, obj):
        # return f"http://127.0.0.1:8000/api/upde/{obj.id}/"
        request = self.context.get('request')
        return api_reverse("api-core:upd-del", kwargs={'pk': obj.id}, request=request)


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
    # owner = UserPublicSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    user_uri = serializers.HyperlinkedRelatedField(source='owner',  # user_foreignkey
                                                   lookup_field='username',
                                                   view_name='api-user:detail',
                                                   read_only=True)
    user_email = serializers.SlugRelatedField(source='owner', read_only=True, slug_field='email')
    # owner = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = ['uri', 'id', 'user_email', 'user_uri', 'title', 'description', 'owner', 'image', 'file']
        read_only_fields = ['owner']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-core:upd-del", kwargs={'pk': obj.id}, request=request)
        # ("<namespace>:<url_name or view_name>", kwargs={'username': obj.username}, request=request)
        # return f"http://127.0.0.1:8000/api/upde/{obj.id}/"

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


class PostSerializerUpDe(PostSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = Post
        fields = ['uri', 'id', 'owner', 'title', 'description', 'image', 'file']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-core:upd-del", kwargs={'pk': obj.id}, request=request)


"""-----------------------------------------------------------------------------------------------"""




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['value', 'author', 'body']


class BookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'review']

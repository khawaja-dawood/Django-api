from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from core.serializers import PostInlineUserSerializer
from core.models import Post

user = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    posts = serializers.SerializerMethodField(read_only=True)
    posts_lists = serializers.HyperlinkedRelatedField(source='post_set',  # posts.objects.filter(owner=user)
                                                      many=True, read_only=True, lookup_field='pk',
                                                      view_name='api-core:upd-del')

    class Meta:
        model = user
        fields = ['id', 'username', 'uri', 'posts_lists', 'posts']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:detail", kwargs={'username': obj.username}, request=request)
        # ("<namespace>:<url_name or view_name>", kwargs={'username': obj.username}, request=request)
        # return f"http://127.0.0.1:8000/api/users/{obj.username}/"  # obj.id

    def get_posts(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.post_set.all().order_by("-timestamp")
        data = {
            'uri': self.get_uri(obj) + "posts/",
            'last': PostInlineUserSerializer(qs.first(), context={'request': request}).data,
            'recent_10': PostInlineUserSerializer(qs[:limit], context={'request': request}, many=True).data
        }
        return data

    # def get_post_uri(self, obj):
    #     return self.get_uri(obj) + 'status/'
    #
    # def get_recent_posts(self, obj):
    #     # qs = Post.objects.filter(u)
    #     qs = obj.post_set.all()  # ==> Post.objects.filter(user=obj)
    #     """for limiting data"""  # qs = obj.post_set.all()[:10]
    #     """for reverse ordering by timestamp"""  # qs = obj.post_set.all().order_by("-timestamp")
    #     return PostInlineUserSerializer(qs, many=True).data

from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.serializers import PostInlineUserSerializer
from core.models import Post
user = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    posts = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = user
        fields = ['id', 'username', 'uri', 'posts']

    def get_uri(self, obj):
        return f"http://127.0.0.1:8000/api/users/{obj.username}/"  # obj.id

    def get_posts(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            print(limit_query)
            try:
                limit = int(limit_query)
            except:
                print("fff")
                pass
        qs = obj.post_set.all().order_by("-timestamp")
        data = {
            'uri': self.get_uri(obj) + "posts/",
            'last': PostInlineUserSerializer(qs.first()).data,
            'recent_10': PostInlineUserSerializer(qs[:limit], many=True).data
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
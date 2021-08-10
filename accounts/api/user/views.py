from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, pagination
from accounts.api.user.serializers import UserDetailSerializer
from core.serializers import PostInlineUserSerializer
from accounts.api.permissions import AnonPermissionOnly, IsOwnerOrReadOnly
from core.models import Post
from core.pagination import MyCustomPagination


User = get_user_model()


class UserDetailView(generics.RetrieveAPIView):
    # gets all posts by a specific user with user details also we can also pass a limit argument in to
    # url to limit posts http://127.0.0.1:8000/api/users/f18bb107/?limit=2
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    search_fields = ['owner__username', 'description']
    ordering_fields = ['owner__username', 'timestamp', 'owner__email']

    lookup_field = 'username'  # id

    def get_serializer_context(self):
        return {
            'request': self.request
        }


class UserPostView(generics.ListAPIView):
    # gets all posts by a specific user with no user details
    # http://127.0.0.1:8000/api/users/f18bb107/posts/
    serializer_class = PostInlineUserSerializer
    search_fields = ['owner__username', 'description']
    ordering_fields = ['owner__username', 'timestamp', 'owner__email']
    # pagination_class = MyCustomPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)
        # print(username)
        if username is None:
            return Post.objects.none()
        return Post.objects.filter(owner__username=username)
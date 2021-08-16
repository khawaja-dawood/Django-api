from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post

from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication

from accounts.api.permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, PostSerializerUpDe, BookSerializer
from rest_framework import generics
from rest_framework import mixins, permissions



""" These classes and functions are for get
 and post views"""
# class TestView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


"""This is update delete views"""
# class PostUpdateView(generics.UpdateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#
# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication]

    search_fields = ['owner__username', 'description']
    ordering_fields = ['owner__username', 'timestamp']
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # this override method is for auto filling username which is logged in or POST method for
    # making this field readonly.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostUpdateDeleteView(generics.RetrieveDestroyAPIView, generics.UpdateAPIView):
    # permissions we wanted to be enforced
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # How we wanted to be authenticated
    # authentication_classes = [SessionAuthentication]

    serializer_class = PostSerializerUpDe
    queryset = Post.objects.all()


class getBooksList(generics.ListAPIView):
    # permissions we wanted to be enforced
    permission_classes = [permissions.AllowAny]
    # How we wanted to be authenticated
    # authentication_classes = [SessionAuthentication]

    serializer_class = BookSerializer
    queryset = Post.objects.all()

"""______________________________________________________________________"""

# class StatusAPIView(
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.ListAPIView):
#     permission_classes          = []
#     authentication_classes      = []
#     serializer_class            = StatusSerializer
#     passed_id                   = None

#     def get_queryset(self):
#         request = self.request
#         qs = Status.objects.all()
#         query = request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def get_object(self):
#         request         = self.request
#         passed_id       = request.GET.get('id', None) or self.passed_id
#         queryset        = self.get_queryset()
#         obj = None
#         if passed_id is not None:
#             obj = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)
#         return obj

#     def perform_destroy(self, instance):
#         if instance is not None:
#             return instance.delete()
#         return None

#     def get(self, request, *args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         if passed_id is not None:# or passed_id is not "":
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         print(request.data)
#         requested_id = None #request.data.get('id')
#         passed_id = url_passed_id or new_passed_id or requested_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         url_passed_id    = request.GET.get('id', None)
#         json_data        = {}
#         body_            = request.body
#         if is_json(body_):
#             json_data        = json.loads(request.body)
#         new_passed_id    = json_data.get('id', None)
#         #print(request.body)
#         #request.data
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.destroy(request, *args, **kwargs)


#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


# class StatusListSearchAPIView(APIView):
#     permission_classes          = []
#     authentication_classes      = []

#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)


# # CreateModelMixin --- POST method
# # UpdateModelMixin --- PUT method
# # DestroyModelMixin -- DELETE method

# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView): # Create List
#     permission_classes          = []
#     authentication_classes      = []
#     serializer_class            = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes          = []
#     authentication_classes      = []
#     queryset                    = Status.objects.all()
#     serializer_class            = StatusSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #     permission_classes          = []
# #     authentication_classes      = []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer


# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #     permission_classes          = []
# #     authentication_classes      = []
# #     queryset                    = Status.objects.all()
# #     serializer_class            = StatusSerializer


# # class StatusCreateView(CreateView):
# #     queryset                    = Status.objects.all()
# #     form_class                  = StatusForm

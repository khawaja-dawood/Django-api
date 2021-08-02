from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication

from .serializers import PostSerializer
from rest_framework import generics
from rest_framework import mixins, permissions

from .models import Post

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

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # this override method is for auto filling username which is logged in.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostUpdateDeleteView(generics.RetrieveDestroyAPIView, generics.UpdateAPIView):
    # permissions we wanted to be enforced
    # permission_classes = [permissions.IsAuthenticated]
    # How we wanted to be authenticated
    # authentication_classes = [SessionAuthentication]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PostsList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @api_view(['OPTIONS'])
    def options(self, request, *args, **kwargs):
        return Response()

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @api_view(['OPTIONS'])
    def options(self, request, *args, **kwargs):
        return Response()
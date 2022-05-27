from django.shortcuts import render
from  .models import Post
from .serializers import PostSerializers
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, permissions

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
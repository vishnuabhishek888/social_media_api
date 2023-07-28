from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from posts.models import Post
from user_profile.permissions import IsOwnerOrReadOnly
# from posts.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend

from user_profile.serializers import ProfileSerializer
from user_profile.models import Profile



class SearchViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

# class SearchViewSet(viewsets.ModelViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
#     permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['content']


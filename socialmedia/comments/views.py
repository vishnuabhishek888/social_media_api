from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from .models import Comment
from .serializers import CommentSerializers
from user_profile.permissions import IsOwnerOrReadOnly

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
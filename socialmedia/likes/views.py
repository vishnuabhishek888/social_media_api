from django.shortcuts import render, get_object_or_404
from posts.models import Post
from likes.permissions import hasSelfLikeOrReadOnly
from rest_framework import viewsets, status, permissions, serializers
from .models import Like_Model
from .serializers import LikeSerializers

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset=Like_Model.objects.all()
    serializer_class=LikeSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfLikeOrReadOnly]

    def perform_create(self, serializer):
        post_instance = get_object_or_404(Post, pk=self.request.data['post'])
        like = self.request.data.get('like')  # use get method to avoid MultiValueDictKeyError
        if like:
            already_like = Like_Model.objects.filter(post=post_instance, like_by=self.request.user).exists()
            if already_like:
                raise serializers.ValidationError({"message":"you have already liked this post"})
            else:
                serializer.save(like_by=self.request.user, post=post_instance)

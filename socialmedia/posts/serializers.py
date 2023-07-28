from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializers
from likes.serializers import LikeSerializers
class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializers(many=True, read_only=True)
    likes=LikeSerializers(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id','content','post_image','links','post_date','comments','likes')




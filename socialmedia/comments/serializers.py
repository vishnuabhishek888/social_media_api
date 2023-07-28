from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
    commented_by=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Comment
        fields=('id','post','comment','comment_date','commented_by')

from rest_framework import serializers
from .models import Like_Model
class LikeSerializers(serializers.ModelSerializer):
    like_by=serializers.ReadOnlyField(source='like_by.username')
    class Meta:
        model=Like_Model
        fields=('id','post','like_by')
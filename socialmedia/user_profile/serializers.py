from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Profile
        fields='__all__'
        
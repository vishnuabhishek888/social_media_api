from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile.serializers import ProfileSerializer

class UserSerializers(serializers.ModelSerializer):
    profile_data=ProfileSerializer(read_only=True)
    class Meta:
        model=User
        fields = ('id','username', 'email','password','is_active', 'profile_data')
        extra_kwargs={'email':{'required':True,'write_only':True},'password':{'write_only':True}}

    def create(self,validate_data):
        user=User(
            email=validate_data['email'],
            username=validate_data['username']
        )

        user.set_password(validate_data['password'])
        user.save()
        return user 

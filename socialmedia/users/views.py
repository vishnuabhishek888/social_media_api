from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializers

# Create your views here.

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def list(self,request):
        queryset=User.objects.all()
        serializer=UserSerializers(queryset,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk):
        queryset=User.objects.all()
        user=get_object_or_404(queryset,pk=pk)
        serializer=UserSerializers(user)
        return Response(serializer.data)
    
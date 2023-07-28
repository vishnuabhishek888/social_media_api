from django.db import models
from posts.models import Post

# Create your models here.

class Like_Model(models.Model):
    post=models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)
    like=models.ForeignKey('auth.User',related_name='like_user',on_delete=models.CASCADE, default=None, blank=True, null=True)
    def __str__(self):
        return self.post.content
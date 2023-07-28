from django.db import models

# Create your models here.
class Post(models.Model):
    owner=models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    links=models.URLField(null=True,blank=True)
    post_image=models.ImageField(upload_to="post_image",null=True,blank=True)
    post_date= models.DateField(auto_now_add=True)
    def __str__(self):
        return self.content


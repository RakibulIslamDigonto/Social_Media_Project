from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    images = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Mete():
        ordering=['-upload_date']


class Liked(models.Model):
    post=models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='liked_post')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.formate(self.user, self.posts)

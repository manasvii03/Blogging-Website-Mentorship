from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Blog

# Create your models here.

#class Favourites(models.Model):
#    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True)
#
#    class Meta:
#        unique_together = ('user', 'blog')
#
#    def __str__(self):
#        return f"{self.user.username} favorited {self.blog.title}"
#
#class Reading_List(models.Model):
#    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True)
#
#    class Meta:
#        unique_together = ('user', 'blog')
#
#    def __str__(self):
#        return f"{self.user.username} read {self.blog.title}"
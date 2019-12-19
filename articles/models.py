from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='written_comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
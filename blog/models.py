from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    author = models.CharField(max_length = 40)

    def __str__(self):
        return self.title

class PostComment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.comment

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from jwt_auth.models import User

# Create your models here.


class Post(models.Model):
    """
    Stores a single blog post entry
    `ordering` by `date` in descending order
    """
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField()
    thumbnail = models.ImageField()
    excerpt = RichTextUploadingField(max_length=600)
    content = RichTextUploadingField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def comments_count(self):
        return self.comments.all().count()

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    """
    Stores a single post comment entry
    `ordering` by `id` in descending order
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-id']

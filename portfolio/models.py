from django.db import models
from django.core.validators import MinLengthValidator
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class PortfolioProject(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(upload_to='projects')
    excerpt = RichTextUploadingField(
        max_length=600, validators=[MinLengthValidator(10)])
    content = RichTextUploadingField(validators=[MinLengthValidator(10)])

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

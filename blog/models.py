from django.db import models
from django.contrib.auth.models import User


# def validate_file_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value)[1]
#     valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
#     if ext.lower() in valid_extensions:
#         raise ValidationError('Unsupported file extension')


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="files/user_avatar/", null=True, blank=True)
    description = models.CharField(max_length=512, null=False, blank=False)


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to="files/article_cover/", null=True, blank=True,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)



class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to="files/category_cover/", null=True, blank=True)


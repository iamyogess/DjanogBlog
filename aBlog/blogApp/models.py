from django.db import models
from django.contrib.auth.models import User


class AddBlogModel(models.Model):
    title = models.CharField(max_length=255)
    blog_content = models.TextField()
    blog_img = models.ImageField(blank=True, null=True,upload_to='images')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    # def __str__(self):
    #     return self.title + '\n' + self.blog_content
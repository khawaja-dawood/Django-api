from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', default=None, null=True, blank=True)
    file = models.FileField(upload_to='files', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    # @property
    # def user(self):
    #     return self.owner







class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Review(models.Model):

    value = models.CharField(max_length=50)
    project = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, max_length=300, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.value
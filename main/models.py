from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(User)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)




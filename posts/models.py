from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from categories.models import Category


class Post(models.Model):
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField()
    share = models.IntegerField()
    def __str__(self):
        return self.category 
    
class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.reviewer.user.first_name}" 
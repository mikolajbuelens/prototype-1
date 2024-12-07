from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    source= models.CharField(null=True, max_length=100) 
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.title
    
    
 
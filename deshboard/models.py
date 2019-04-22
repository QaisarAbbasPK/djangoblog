from django.db import models

# Create your models here.

class Posts(models.Model):
    fname   = models.CharField(max_length=200)
    lname   = models.CharField(max_length=200)
    phone   = models.CharField(max_length=200)
    email   = models.EmailField(max_length=70)
    address = models.CharField(max_length=200)



class Article(models.Model):
    title = models.CharField(max_length=100)
    body  = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)    


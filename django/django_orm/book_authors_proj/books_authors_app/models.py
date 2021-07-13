from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books =  models.ManyToManyField(book, related_name="authors")
    notas = models.TextField(default="notas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
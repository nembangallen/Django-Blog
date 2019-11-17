from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.title
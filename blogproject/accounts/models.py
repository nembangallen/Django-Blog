from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='user/')
    
    def __str__(self):
        return self.user.username
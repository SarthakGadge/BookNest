from django.db import models
from userauth.models import CustomUser


class UserDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    bio = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="static/download.png",upload_to='post_images/', blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
# Create your models here.

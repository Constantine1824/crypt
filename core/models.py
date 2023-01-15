from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PasswordModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hashedPw = models.CharField(max_length=356,blank=False)
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_username()

# Create your models here.

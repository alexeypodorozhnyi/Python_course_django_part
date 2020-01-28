from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email_token = models.CharField(max_length=100,blank=True,null=True)
    email_is_confirmed = models.BooleanField(default=False)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='My note')
    text = models.TextField(null=True, blank=True)
    is_shared = models.BooleanField(default=False)

    def __str__(self):
        return self.name

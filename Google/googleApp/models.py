from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/%y', null=True, blank=True)


class Chat_GPT(models.Model):
    user_message = models.TextField(default='')
    gpt_message = models.TextField(default='')
    def __str__(self):
        return self.user_message, self.gpt_message



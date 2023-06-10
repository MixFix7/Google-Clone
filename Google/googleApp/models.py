from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class ChatGPTHistory(models.Model):
    user_message = models.TextField(default='')
    gpt_message = models.TextField(default='')
    name = models.CharField(max_length=30, default="", editable=False)

    def __str__(self):
        return f"{self.name}: {self.user_message} GPT: {self.gpt_message}"


class ProfileSearche(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    search = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}. {self.user.name}: {self.search}"

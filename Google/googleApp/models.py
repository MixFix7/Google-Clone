from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class ChatGPTHistory(models.Model):
    user_message = models.TextField(default='')
    gpt_message = models.TextField(default='')
    name = models.CharField(max_length=30, default="", editable=False)
    def __str__(self):
        return f"{self.name}: {self.user_message} GPT: {self.gpt_message}"




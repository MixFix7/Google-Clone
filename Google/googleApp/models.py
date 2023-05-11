from django.db import models


class Chat_GPT(models.Model):
    user_message = models.TextField(default='')
    gpt_message = models.TextField(default='')
    def __str__(self):
        return self.user_message, self.gpt_message



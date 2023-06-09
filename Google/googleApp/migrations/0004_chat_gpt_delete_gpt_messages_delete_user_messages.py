# Generated by Django 4.2.1 on 2023-05-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleApp', '0003_gpt_messages_user_messages_delete_chat_with_gpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_GPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.TextField(default='')),
                ('gpt_message', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='GPT_messages',
        ),
        migrations.DeleteModel(
            name='User_messages',
        ),
    ]

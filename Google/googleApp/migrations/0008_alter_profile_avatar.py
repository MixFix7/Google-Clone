# Generated by Django 4.2.1 on 2023-05-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleApp', '0007_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]

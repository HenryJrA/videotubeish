# Generated by Django 3.2.7 on 2021-09-09 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_video_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videoFile',
            field=models.FileField(upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
# Generated by Django 4.2.16 on 2024-12-05 13:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_time_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
# Generated by Django 4.2.16 on 2024-12-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_comment_options_alter_event_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.IntegerField(choices=[(0, '---'), (1, 'Witchcraft for begginers'), (2, 'Spells & Rituals'), (3, 'Witch-Crafts'), (4, 'Music & Dance'), (5, 'Foods & Elixirs'), (6, 'Markets & Trading'), (7, 'Healing & Wellness'), (8, 'Dark Arts & Shadow Work'), (9, 'Tarot & Divination'), (10, 'Other')], default=0),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-16 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_room_participants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='describtion',
            new_name='description',
        ),
    ]

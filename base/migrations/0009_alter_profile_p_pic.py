# Generated by Django 4.0.4 on 2022-05-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_profile_p_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='p_pic',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
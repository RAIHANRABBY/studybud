# Generated by Django 4.0.4 on 2022-05-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='p_pic',
            field=models.ImageField(default='default.jpg', upload_to='%Y/%m/%d'),
        ),
    ]
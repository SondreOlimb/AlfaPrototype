# Generated by Django 3.1.2 on 2020-12-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_profile_shoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image_url',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
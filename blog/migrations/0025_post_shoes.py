# Generated by Django 3.1.2 on 2020-12-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_addshoe_link_shoe'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shoes',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
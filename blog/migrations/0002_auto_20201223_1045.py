# Generated by Django 3.1.2 on 2020-12-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='shoes',
        ),
        migrations.AddField(
            model_name='post',
            name='shoes',
            field=models.ManyToManyField(to='blog.Shoe'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-23 13:27

import ckeditor.fields
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201223_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tiny',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

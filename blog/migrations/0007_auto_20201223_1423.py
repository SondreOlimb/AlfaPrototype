# Generated by Django 3.1.2 on 2020-12-23 13:23

import ckeditor_uploader.fields
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201223_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]

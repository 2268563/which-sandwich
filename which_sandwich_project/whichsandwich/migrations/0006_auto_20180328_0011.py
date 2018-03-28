# Generated by Django 2.0.2 on 2018-03-28 00:11

from django.db import migrations
import imagekit.models.fields
import whichsandwich.models


class Migration(migrations.Migration):

    dependencies = [
        ('whichsandwich', '0005_auto_20180327_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=whichsandwich.models.user_directory_path),
        ),
    ]

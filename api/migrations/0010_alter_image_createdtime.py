# Generated by Django 4.2.5 on 2023-09-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='createdTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

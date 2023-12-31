# Generated by Django 4.0.4 on 2023-09-23 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_user_access_level_image_access_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='access_level',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='expiring_link_duration',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=1000)]),
        ),
    ]

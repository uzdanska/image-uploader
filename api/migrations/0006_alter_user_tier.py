# Generated by Django 4.2.5 on 2023-09-21 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.thumbnail'),
        ),
    ]
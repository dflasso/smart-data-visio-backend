# Generated by Django 4.0.1 on 2022-01-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Security', '0002_resourcesprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

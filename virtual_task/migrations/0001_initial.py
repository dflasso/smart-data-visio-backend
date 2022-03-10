# Generated by Django 4.0.1 on 2022-03-10 09:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualTaskResultsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_virtual_task', models.CharField(max_length=300)),
                ('code_virtual_task', models.CharField(max_length=50)),
                ('total_hits', models.FloatField()),
                ('total_errors', models.FloatField()),
                ('group_test_ophthalmological', models.CharField(max_length=50)),
            ],
        ),
    ]
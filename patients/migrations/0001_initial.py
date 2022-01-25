# Generated by Django 4.0.1 on 2022-01-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id_diseases', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('indications', models.CharField(blank=True, max_length=300)),
                ('observations', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EyeglassesPatient',
            fields=[
                ('id_eyeglasses', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('use', models.BooleanField()),
                ('measurement', models.FloatField(null=True)),
                ('started_use_at', models.DateTimeField(null=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]

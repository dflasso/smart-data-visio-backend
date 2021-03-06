# Generated by Django 4.0.1 on 2022-02-03 03:30

from django.db import migrations, models
import djongo.models.fields
import questionnaires.models.questionnaire
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id_question', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('statement', models.CharField(max_length=100)),
                ('answerLabel', models.CharField(max_length=100)),
                ('answerValue', models.FloatField()),
                ('answerMinValue', models.FloatField()),
                ('answerMaxValue', models.FloatField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionnaireModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('num_test_group', models.CharField(max_length=50)),
                ('code_virtual_task', models.CharField(max_length=50)),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
                ('observations', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('questions', djongo.models.fields.ArrayField(model_container=questionnaires.models.questionnaire.QuestionModel)),
            ],
        ),
    ]

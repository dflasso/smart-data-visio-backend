# Generated by Django 4.0.1 on 2022-01-29 20:20

from django.db import migrations, models
import legal_documents.models.virtual_test_docs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualTestDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_test', models.CharField(max_length=50)),
                ('code_virtual_test', models.CharField(max_length=10)),
                ('name_virtual_test', models.CharField(max_length=100)),
                ('type_doc', models.CharField(max_length=100)),
                ('code_type_doc', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('document', models.FileField(blank=True, null=True, upload_to=legal_documents.models.virtual_test_docs.doc_directory_path)),
            ],
        ),
    ]
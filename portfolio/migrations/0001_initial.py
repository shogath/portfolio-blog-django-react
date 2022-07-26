# Generated by Django 4.0.5 on 2022-07-16 16:40

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('excerpt', ckeditor_uploader.fields.RichTextUploadingField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)])),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
    ]

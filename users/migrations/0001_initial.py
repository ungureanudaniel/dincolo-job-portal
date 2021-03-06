# Generated by Django 3.2.12 on 2022-04-08 20:02

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=600)),
                ('image1', models.ImageField(blank=True, upload_to='about_image')),
                ('image2', models.ImageField(blank=True, upload_to='about_image')),
                ('image3', models.ImageField(blank=True, upload_to='about_image')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.FileField(blank=True, upload_to='media')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, upload_to='media')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('type', models.CharField(default='freelancer', max_length=15)),
                ('conf_number', models.CharField(max_length=15)),
                ('confirmed', models.BooleanField(default=False)),
                ('status', models.CharField(default='verification pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]

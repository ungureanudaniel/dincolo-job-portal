# Generated by Django 3.2.12 on 2022-04-08 20:38

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import recruiters.models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='company_logos')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('locality', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('skills_req', models.CharField(max_length=200)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Remote', 'Remote')], default='Full Time', max_length=30, null=True)),
                ('from_wage_hour', models.IntegerField(null=True)),
                ('to_wage_hour', models.IntegerField(null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default=recruiters.models.JobCategory.get_default_pk, on_delete=django.db.models.deletion.CASCADE, related_name='job_category', to='recruiters.jobcategory')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
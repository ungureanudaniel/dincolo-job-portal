# Generated by Django 3.2.8 on 2021-10-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0011_alter_jobcategory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcategory',
            name='icon',
            field=models.ImageField(blank=True, upload_to='media/job_category'),
        ),
    ]

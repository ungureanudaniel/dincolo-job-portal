# Generated by Django 3.2.8 on 2021-10-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0015_alter_jobcategory_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
    ]

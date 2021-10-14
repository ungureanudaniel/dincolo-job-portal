# Generated by Django 3.2.8 on 2021-10-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0002_auto_20211014_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selected',
            options={'verbose_name': 'Selected', 'verbose_name_plural': 'Selected'},
        ),
        migrations.AddField(
            model_name='job',
            name='from_wage_hour',
            field=models.IntegerField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='to_wage_hour',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]
# Generated by Django 3.1.2 on 2021-01-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shorten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='browser',
            field=models.CharField(max_length=1000),
        ),
    ]
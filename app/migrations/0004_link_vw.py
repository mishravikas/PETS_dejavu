# Generated by Django 2.1.5 on 2020-08-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200819_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='vw',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
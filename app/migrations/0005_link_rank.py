# Generated by Django 2.1.5 on 2020-08-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_link_vw'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='rank',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

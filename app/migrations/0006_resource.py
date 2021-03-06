# Generated by Django 2.1.5 on 2020-08-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_link_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('rank', models.CharField(max_length=500, null=True)),
                ('website', models.CharField(max_length=500)),
                ('secret', models.CharField(max_length=500, null=True)),
                ('vw', models.CharField(max_length=500, null=True)),
                ('inUse', models.BooleanField(default=False)),
            ],
        ),
    ]

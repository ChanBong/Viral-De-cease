# Generated by Django 3.1.5 on 2021-01-10 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0002_auto_20210109_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseas',
            name='about_l',
        ),
        migrations.RemoveField(
            model_name='diseas',
            name='symptoms',
        ),
    ]
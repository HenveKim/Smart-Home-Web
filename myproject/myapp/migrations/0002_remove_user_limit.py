# Generated by Django 5.0 on 2023-12-21 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='limit',
        ),
    ]
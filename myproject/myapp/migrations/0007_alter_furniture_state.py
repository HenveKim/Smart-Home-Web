# Generated by Django 5.0 on 2023-12-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_room_num_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='state',
            field=models.SmallIntegerField(choices=[(0, '关'), (1, '开')], default=0, verbose_name='状态'),
        ),
    ]

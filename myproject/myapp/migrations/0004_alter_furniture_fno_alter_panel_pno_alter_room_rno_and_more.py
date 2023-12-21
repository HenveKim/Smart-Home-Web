# Generated by Django 5.0 on 2023-12-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_account_user_email_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='fno',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='fno号'),
        ),
        migrations.AlterField(
            model_name='panel',
            name='pno',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='pno号'),
        ),
        migrations.AlterField(
            model_name='room',
            name='rno',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='rno号'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='rno',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='rno号'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sno',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='sno号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='uid号'),
        ),
    ]
# Generated by Django 3.2.16 on 2023-02-17 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0004_auto_20230217_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='foydalanuvchi',
        ),
    ]

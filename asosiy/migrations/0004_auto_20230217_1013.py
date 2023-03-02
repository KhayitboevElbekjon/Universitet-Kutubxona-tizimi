# Generated by Django 3.2.16 on 2023-02-17 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0003_alter_admin_ish_vaqti'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talaba',
            options={'ordering': ('ism',)},
        ),
        migrations.AddField(
            model_name='record',
            name='foydalanuvchi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
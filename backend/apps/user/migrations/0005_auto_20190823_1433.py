# Generated by Django 2.0.4 on 2019-08-23 06:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190820_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('1add3b96-99a7-4d63-a9d8-fc3d7d25d268'), verbose_name='用户jwt加密秘钥'),
        ),
    ]

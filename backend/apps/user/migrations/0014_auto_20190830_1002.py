# Generated by Django 2.0.4 on 2019-08-30 02:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20190829_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('1d47acd3-cba8-4a66-a460-4e355fec0c8d'), verbose_name='用户jwt加密秘钥'),
        ),
    ]

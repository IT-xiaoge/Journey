# Generated by Django 2.1.1 on 2020-02-21 17:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200221_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('728f869b-1f15-476d-a4d7-07508d54d657'), verbose_name='用户jwt加密秘钥'),
        ),
    ]

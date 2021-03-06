# Generated by Django 2.0.4 on 2019-12-27 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_auto_20191227_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('73a6dbbe-f024-4109-878e-fbaa34eab09b'), verbose_name='用户jwt加密秘钥'),
        ),
    ]

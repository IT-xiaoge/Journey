# Generated by Django 2.0.4 on 2019-12-10 03:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20190903_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('3fe63a54-b5c7-4bc6-a506-4ada112955da'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
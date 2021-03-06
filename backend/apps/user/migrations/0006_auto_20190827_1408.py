# Generated by Django 2.0.4 on 2019-08-27 06:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190823_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '菜单表', 'verbose_name_plural': '菜单表'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': '角色表', 'verbose_name_plural': '角色表'},
        ),
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('b7b001cc-7f0f-46bf-a689-a589c1aa5ca8'), verbose_name='用户jwt加密秘钥'),
        ),
    ]

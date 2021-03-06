# Generated by Django 2.0.4 on 2019-07-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20190704_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='MongoDBInst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inst_name', models.CharField(max_length=128, verbose_name='MongoDBInst名称')),
                ('inst_host', models.GenericIPAddressField(verbose_name='MongoDBInstIP地址')),
                ('inst_port', models.PositiveIntegerField(verbose_name='MongoDBInst端口')),
                ('manage_user', models.CharField(blank=True, max_length=32, verbose_name='MongoDBInst管理用户')),
                ('manage_userpwd', models.CharField(blank=True, max_length=64, verbose_name='MongoDBInst管理用户密码')),
                ('read_user', models.CharField(blank=True, max_length=32, verbose_name='MongoDBInst只读用户')),
                ('read_userpwd', models.CharField(blank=True, max_length=32, verbose_name='MongoDBInst只读用户密码')),
                ('role', models.CharField(blank=True, choices=[('Master', 'Master'), ('Slave', 'Slave')], default='Master', max_length=12, verbose_name='是否启用')),
                ('services', models.CharField(blank=True, max_length=255, verbose_name='涉及服务')),
                ('version', models.CharField(blank=True, default='5.7.21', max_length=32, verbose_name='MongoDB版本')),
                ('is_enabled', models.CharField(choices=[('ENABLED', 'ENABLED'), ('DISABLED', 'DISABLED')], default='ENABLED', max_length=12, verbose_name='是否启用')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('comment', models.CharField(blank=True, max_length=64, verbose_name='备注')),
            ],
            options={
                'verbose_name': 'MongoDB实例',
                'verbose_name_plural': 'MongoDB实例',
            },
        ),
    ]

# Generated by Django 2.0.4 on 2019-07-16 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0014_auto_20190715_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccessRedis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '已禁止'), (1, '申请中'), (2, '使用中'), (3, '已驳回')], default=1, verbose_name='用户申请查询权限状态')),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('redisinst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_access_redisinst', to='db.RedisInst', verbose_name='Redis实例id')),
            ],
            options={
                'verbose_name': '用户访问Redis权限表',
                'verbose_name_plural': '用户访问Redis权限表',
            },
        ),
    ]

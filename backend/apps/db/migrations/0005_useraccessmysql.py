# Generated by Django 2.0.4 on 2019-06-05 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_auto_20190604_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccessMySQL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('user_access_db', models.CharField(max_length=64, verbose_name='用户访问数据库')),
                ('life_time', models.IntegerField(verbose_name='MYSQL用户访问权限时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('expired_time', models.DateTimeField(blank=True, verbose_name='MYSQL用户访问权限到期时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '已到期'), (1, '申请中'), (2, '使用中'), (3, '已驳回')], default=1, verbose_name='用户申请查询权限状态')),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('mysqlinst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_access_mysqlinst', to='db.MySQLInst', verbose_name='MYSQL实例id')),
            ],
            options={
                'verbose_name': 'MYSQL用户权限时间表',
                'verbose_name_plural': 'MYSQL用户权限时间表',
            },
        ),
    ]

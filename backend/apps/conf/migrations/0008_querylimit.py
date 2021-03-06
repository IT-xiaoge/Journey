# Generated by Django 2.0.4 on 2019-06-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0007_delete_ldapconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryLimit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_type', models.CharField(blank=True, max_length=64, verbose_name='查询类型')),
                ('query_limit', models.IntegerField(blank=True, default=25, verbose_name='查询LIMIT')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('comment', models.CharField(blank=True, max_length=64, verbose_name='备注')),
            ],
            options={
                'verbose_name': '查询limit配置',
                'verbose_name_plural': '查询limit配置',
            },
        ),
    ]

# Generated by Django 2.0.4 on 2019-08-28 07:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0002_auto_20190827_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver_group_name', models.CharField(blank=True, max_length=128, verbose_name='工单审批组')),
                ('user', models.ManyToManyField(blank=True, related_name='approver_user', to=settings.AUTH_USER_MODEL, verbose_name='审批组内用户')),
            ],
            options={
                'verbose_name': '工单审批组表',
                'verbose_name_plural': '工单审批组表',
            },
        ),
    ]

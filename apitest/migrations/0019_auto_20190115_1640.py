# Generated by Django 2.1.2 on 2019-01-15 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0018_auto_20190110_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='apimethod',
            field=models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, verbose_name='请求方法'),
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='apiname',
            field=models.CharField(max_length=100, verbose_name='接口名称'),
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='apiresponse',
            field=models.TextField(max_length=5000, verbose_name='响应数据json'),
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='apiurl',
            field=models.CharField(max_length=200, verbose_name='url地址'),
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='bodytype',
            field=models.CharField(choices=[('application/json;charset=utf-8', 'application/json;charset=utf-8'), ('application/x-www-form-urlencoded', 'application/x-www-form-urlencoded')], default='json', max_length=200, verbose_name='body类型'),
        ),
        migrations.AlterField(
            model_name='apis',
            name='apitester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='测试负责人'),
        ),
    ]

# Generated by Django 2.1.2 on 2019-01-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0020_apis_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiinfo',
            name='level',
            field=models.IntegerField(default=-1, verbose_name='测试基本'),
        ),
    ]

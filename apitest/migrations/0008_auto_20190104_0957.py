# Generated by Django 2.1.2 on 2019-01-04 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0007_auto_20190102_1104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apitest',
            options={'ordering': ['-create_time'], 'verbose_name': '流程场景接口', 'verbose_name_plural': '流程场景接口'},
        ),
    ]

# Generated by Django 2.1.7 on 2019-06-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0005_auto_20190531_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualification',
            name='part_time',
        ),
        migrations.AlterField(
            model_name='qualification',
            name='full_time',
            field=models.BooleanField(blank=True, help_text='Can this qualification be completed on a full-time basis?', null=True),
        ),
    ]

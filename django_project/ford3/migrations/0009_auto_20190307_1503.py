# Generated by Django 2.1.5 on 2019-03-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0008_auto_20190307_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='telephone',
            field=models.BigIntegerField(null=True),
        ),
    ]

# Generated by Django 2.1.5 on 2019-03-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0005_qualificationevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_type',
            field=models.CharField(default='', max_length=255),
        ),
    ]

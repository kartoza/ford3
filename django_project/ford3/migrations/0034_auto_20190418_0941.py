# Generated by Django 2.1.7 on 2019-04-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0033_auto_20190416_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='provider',
            name='provider_logo',
            field=models.ImageField(blank=True, upload_to='provider_logo'),
        ),
    ]
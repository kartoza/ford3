# Generated by Django 2.1.5 on 2019-03-07 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0004_campusevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualificationEvent',
            fields=[
                ('id', models.IntegerField(help_text='Key of qualification event', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('http_link', models.CharField(max_length=255)),
                ('qualification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Qualification')),
            ],
        ),
    ]

# Generated by Django 3.0.1 on 2020-01-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0003_androidscrape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='androidscrape',
            name='percent',
            field=models.IntegerField(max_length=4),
        ),
    ]

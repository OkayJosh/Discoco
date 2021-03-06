# Generated by Django 3.0.1 on 2020-01-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.CharField(max_length=4)),
                ('product', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
                ('old_price', models.CharField(max_length=10)),
                ('product_url', models.URLField(max_length=300, unique=True)),
                ('img_url', models.URLField(max_length=300)),
            ],
        ),
    ]

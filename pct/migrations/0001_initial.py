# Generated by Django 2.0.5 on 2018-05-24 18:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HalfmileWaypoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('name', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('elevation', models.FloatField(blank=True, null=True)),
                ('symbol', models.TextField(blank=True)),
            ],
        ),
    ]

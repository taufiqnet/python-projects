# Generated by Django 3.2.16 on 2022-12-05 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20221205_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mod_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]

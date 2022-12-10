# Generated by Django 3.2.16 on 2022-12-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

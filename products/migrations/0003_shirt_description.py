# Generated by Django 4.2.6 on 2024-03-01 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_shirt_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

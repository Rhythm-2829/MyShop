# Generated by Django 4.2.6 on 2024-03-01 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='brand',
            field=models.CharField(max_length=70, null=True),
        ),
    ]

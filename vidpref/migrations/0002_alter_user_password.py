# Generated by Django 3.2.7 on 2024-05-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidpref', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

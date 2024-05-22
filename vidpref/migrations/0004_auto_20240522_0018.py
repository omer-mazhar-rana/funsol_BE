# Generated by Django 3.2.7 on 2024-05-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidpref', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('news', 'News'), ('comedy', 'Comedy'), ('infotainment', 'Infotainment'), ('entertainment', 'Entertainment'), ('romance', 'Romance'), ('tech', 'Tech'), ('sciFi', 'SciFi'), ('movies', 'Movies'), ('thriller', 'Thriller')], max_length=20, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_preference',
        ),
        migrations.AddField(
            model_name='user',
            name='user_preference',
            field=models.ManyToManyField(blank=True, to='vidpref.Genre'),
        ),
    ]
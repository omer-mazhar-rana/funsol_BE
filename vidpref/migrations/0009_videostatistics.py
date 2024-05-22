# Generated by Django 3.2.7 on 2024-05-22 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vidpref', '0008_auto_20240522_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_type', models.CharField(choices=[('View', 'View'), ('Share', 'Share'), ('Download', 'Download')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vidpref.video')),
            ],
        ),
    ]
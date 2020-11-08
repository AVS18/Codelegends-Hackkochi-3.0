# Generated by Django 3.1.2 on 2020-11-07 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20201108_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAnnouncement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=2048)),
                ('date', models.DateField(auto_now_add=True)),
                ('announce_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
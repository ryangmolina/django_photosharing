# Generated by Django 2.1.2 on 2018-10-19 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='invited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invite_invited', to=settings.AUTH_USER_MODEL),
        ),
    ]

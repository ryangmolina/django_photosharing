# Generated by Django 2.1.2 on 2018-10-19 03:22

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photosharing', '0004_auto_20181019_0027'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='invite',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='invite',
            name='inviter',
        ),
        migrations.RemoveField(
            model_name='invite',
            name='user',
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ryan/photosharing/photosharing_site/media'), upload_to='media/'),
        ),
        migrations.DeleteModel(
            name='Invite',
        ),
    ]

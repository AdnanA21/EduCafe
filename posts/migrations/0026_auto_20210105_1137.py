# Generated by Django 3.1.3 on 2021-01-05 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_auto_20210105_1134'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
    ]

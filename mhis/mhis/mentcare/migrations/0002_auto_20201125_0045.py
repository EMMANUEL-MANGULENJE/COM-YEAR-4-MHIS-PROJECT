# Generated by Django 3.1.1 on 2020-11-25 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='home_distric',
            new_name='home_district',
        ),
    ]

# Generated by Django 3.1.1 on 2020-12-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare', '0017_delete_male_rehabilitation_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Male_Rehabilitation_Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentcare.patient')),
            ],
        ),
    ]

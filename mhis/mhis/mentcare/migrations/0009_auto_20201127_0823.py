# Generated by Django 3.1.1 on 2020-11-27 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentcare', '0008_auto_20201127_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tribe', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='Education_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentcare.education'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentcare.tribe'),
        ),
    ]

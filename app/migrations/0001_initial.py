# Generated by Django 4.2.6 on 2023-12-08 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Capitals',
            fields=[
                ('capital_id', models.IntegerField(primary_key=True, serialize=False)),
                ('capitals_name', models.CharField(max_length=100)),
                ('country_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]

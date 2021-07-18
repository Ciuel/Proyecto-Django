# Generated by Django 3.2.5 on 2021-07-18 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('level', models.SmallIntegerField(max_length=1)),
                ('token', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('age', models.PositiveSmallIntegerField(blank=True, max_length=4)),
                ('config', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.config')),
            ],
        ),
    ]
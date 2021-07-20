# Generated by Django 3.2.5 on 2021-07-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210720_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='config',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='coincidences',
            field=models.SmallIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='defeat_text',
            field=models.CharField(default='Perdiste!', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.CharField(default='img', max_length=3),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='victory_text',
            field=models.CharField(default='Ganaste!', max_length=100),
        ),
        migrations.DeleteModel(
            name='Config',
        ),
    ]

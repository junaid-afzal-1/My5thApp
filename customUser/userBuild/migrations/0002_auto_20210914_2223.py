# Generated by Django 3.2.7 on 2021-09-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userBuild', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]

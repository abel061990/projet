# Generated by Django 2.0.5 on 2018-05-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='notebook',
            field=models.IntegerField(default=0),
        ),
    ]
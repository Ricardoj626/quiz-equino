# Generated by Django 2.0.5 on 2018-05-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180506_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='pontuacao',
            field=models.IntegerField(default=0),
        ),
    ]

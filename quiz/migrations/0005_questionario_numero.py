# Generated by Django 2.0.5 on 2018-05-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20180514_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario',
            name='numero',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Número de matrícula'),
        ),
    ]

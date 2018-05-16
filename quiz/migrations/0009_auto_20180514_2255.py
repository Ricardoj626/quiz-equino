# Generated by Django 2.0.5 on 2018-05-15 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20180514_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_1',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 1'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_10',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 10'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_2',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 2'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_3',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 3'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_4',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 4'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_5',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 5'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_6',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 6'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_7',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 7'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_8',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 8'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pergunta_9',
            field=models.CharField(choices=[(0, 'Resposta 1'), (10, 'Resposta 2'), (0, 'Resposta 3')], default=0, max_length=200, verbose_name='Texto da pergunta 9'),
        ),
    ]

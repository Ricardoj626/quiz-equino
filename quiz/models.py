from django.db import models
from multiselectfield import MultiSelectField

CH_PERGUNTA_1 = [
    ('1','Resposta 1'),
    ('10','Resposta 2'),
    ('2','Resposta 3')
]


class Questionario(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(primary_key=True,max_length=6, verbose_name='Número de matrícula')
    pergunta_1 = models.CharField(max_length=200,verbose_name='Texto da pergunta 1', choices=CH_PERGUNTA_1,null=True)
    pergunta_2 = models.CharField(max_length=200,verbose_name='Texto da pergunta 2', choices=CH_PERGUNTA_1,null=True)
    pergunta_3 = models.CharField(max_length=200,verbose_name='Texto da pergunta 3', choices=CH_PERGUNTA_1,null=True)
    pergunta_4 = models.CharField(max_length=200,verbose_name='Texto da pergunta 4', choices=CH_PERGUNTA_1,null=True)
    pergunta_5 = models.CharField(max_length=200,verbose_name='Texto da pergunta 5', choices=CH_PERGUNTA_1,null=True)
    pergunta_6 = models.CharField(max_length=200,verbose_name='Texto da pergunta 6', choices=CH_PERGUNTA_1,null=True)
    pergunta_7 = models.CharField(max_length=200,verbose_name='Texto da pergunta 7', choices=CH_PERGUNTA_1,null=True)
    pergunta_8 = models.CharField(max_length=200,verbose_name='Texto da pergunta 8', choices=CH_PERGUNTA_1,null=True)
    pergunta_9 = models.CharField(max_length=200,verbose_name='Texto da pergunta 9', choices=CH_PERGUNTA_1,null=True)
    pergunta_10 = models.CharField(max_length=200,verbose_name='Texto da pergunta 10', choices=CH_PERGUNTA_1,null=True)

    pontuacao = models.IntegerField(default=0)


    def __str__(self):
        return "{nome} - {pontos}".format(nome=self.nome, pontos=self.pontuacao)





from django.db import models
from multiselectfield import MultiSelectField

CH_PERGUNTA_1 = [
    ('1','Opção a'),
    ('10','Opção b'),
    ('2','Opção c')
]





class Questionario(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(primary_key=True,max_length=6, verbose_name='Número de matrícula')
    pergunta_1 = models.CharField(max_length=200,verbose_name='A partir de uma preocupação da sociedade pós-guerra, foram estabelecidas as “Cinco Liberdades”, que funcionam como fundamentos para as diversas formas de criação e manejo dos animais de produção (Farm Animal Welfare Council, 2009)”, são elas:', choices=CH_PERGUNTA_1,null=True)
    pergunta_2 = models.CharField(max_length=200,verbose_name='É preciso avaliar o grau de bem-estar animal para melhorarmos a qualidade de vida dos cavalos. Existem indicadores diretos e indiretos para essa avaliação, qual alternativa os descreve melhor? ', choices=CH_PERGUNTA_1,null=True)
    pergunta_3 = models.CharField(max_length=200,verbose_name='Sabendo que o cavalo é por natureza uma presa, quais são as suas prioridades para viver da maneira mais natural?', choices=CH_PERGUNTA_1,null=True)
    pergunta_4 = models.CharField(max_length=200,verbose_name='Quando se trata de bem-estar animal, é necessário reconhecer o comportamento natural da espécie em questão. Durante os momentos de interação social, os cavalos apresentam o grooming, do que se trata? ', choices=CH_PERGUNTA_1,null=True)
    pergunta_5 = models.CharField(max_length=200,verbose_name='Sobre o bem-estar animal dos equinos, escolha a alternativa correta: ', choices=CH_PERGUNTA_1,null=True)
    pergunta_6 = models.CharField(max_length=200,verbose_name='Ainda sobre bem-estar animal de equinos, selecione a alternativa incorreta', choices=CH_PERGUNTA_1,null=True)
    pergunta_7 = models.CharField(max_length=200,verbose_name='O surgimento de comportamentos anormais e estereotipias indicam práticas de manejo incorretas. A respeito dessa afirmativa, escolha a alterativa incorreta: ', choices=CH_PERGUNTA_1,null=True)
    pergunta_8 = models.CharField(max_length=200,verbose_name='Assinale a alternativa correta a respeito dos indicadores diretos de bem-estar que podem ser observados nos animais: ', choices=CH_PERGUNTA_1,null=True)
    pergunta_9 = models.CharField(max_length=200,verbose_name='Qual o tipo de cerca mais indicado, visando o bem-estar dos equinos? ', choices=CH_PERGUNTA_1,null=True)
    pergunta_10 = models.CharField(max_length=200,verbose_name='Marque a alternativa que contenha APENAS indicadores INDIRETOS de bem-estar animal: ', choices=CH_PERGUNTA_1,null=True)

    pontuacao = models.IntegerField(default=0)


    def __str__(self):
        return "{nome} - {pontos}".format(nome=self.nome, pontos=self.pontuacao)





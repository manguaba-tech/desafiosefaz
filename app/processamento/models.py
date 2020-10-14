from django.db import models
from app.base.models import Produto


class Regra(models.Model):
    campo = models.CharField('Campo', max_length=50)
    valor = models.CharField('Valor', max_length=50)

    class Meta:
        verbose_name = 'Regra'
        verbose_name_plural = 'Regras'

    def __str__(self):
        return self.campo

class Classificacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    regra = models.ForeignKey(Regra, on_delete=models.CASCADE)
    resultado = models.BooleanField('Resultado', default=False)

    class Meta:
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'

    def __str__(self):
        return self.produto.codigo_gtin



from django.db import models

class Produto(models.Model):
    cor         = models.CharField('Cor', max_length=30)
    codigo_gtin = models.CharField('Codigo Gtin', max_length=20)
    tipo        = models.CharField('Tipo', max_length=50)
    processado  = models.BooleanField('Processado', default=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.codigo_gtin




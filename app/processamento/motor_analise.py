from app.processamento.models import Classificacao, Regra
from app.base.models import Produto


def set_classificacao(pk_produto):
    produto = Produto.objects.get(pk=pk_produto)
    regras = Regra.objects.all()


    for regra in regras:
        if regra.campo == 'cor':
            if regra.valor == produto.cor:
                get_classifica(produto, regra, True)
            else:
                get_classifica(produto, regra, False)

        if regra.campo == 'tipo':
            if regra.valor == produto.tipo:
                get_classifica(produto, regra, True)
            else:
                get_classifica(produto, regra, False)


def get_classifica(produto, regra, resultado):
    classificacao = Classificacao(
        produto=produto,
        regra=regra,
        resultado=resultado
    )
    classificacao.save()


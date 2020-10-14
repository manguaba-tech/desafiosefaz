from app.processamento.models import Classificacao, Regra


def get_produtos_classificados(request):
    try:
       # breakpoint()
        processados = Classificacao.objects.filter(produto__processado=True)
    except:
        processados = None

    return {
        'processados': processados
    }

def get_regras(request):
    try:
        regras = Regra.objects.all()
    except:
        regras = None

    return {
        'regras': regras
    }
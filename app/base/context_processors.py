from app.base.models import Produto

def get_produtos(request):
    try:
        produtos = Produto.objects.all()
    except:
        produtos = None

    return {
        'produtos': produtos
    }

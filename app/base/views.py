from django.views.generic import \
    TemplateView, CreateView, UpdateView, DeleteView
from app.base.forms import ProdutosCreationModelForm
from app.base.models import Produto
from app.processamento.motor_analise import set_classificacao


class Home(TemplateView):
    template_name = 'base/todos_produtos_classificados.html'


class ProdutoCreateView(CreateView):
    template_name = 'base/produtos_formulario.html'
    form_class = ProdutosCreationModelForm
    success_url = '/produto/nova'

    def form_valid(self, form):
        produto = form.save()
        set_classificacao(pk_produto=produto.pk)
        return super().form_valid(form)


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'base/produtos_formulario.html'
    form_class = ProdutosCreationModelForm
    success_url = '/produto/nova'

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'base/produtos_formulario.html'
    form_class = ProdutosCreationModelForm
    success_url = '/produto/nova'




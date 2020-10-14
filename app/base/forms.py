from django.forms import ModelForm
from app.base.models import Produto


class ProdutosCreationModelForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo_gtin','cor','tipo']

from django.urls import path
from app.base.views import \
    ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

app_name = 'base'

urlpatterns = [
    path('nova', ProdutoCreateView.as_view(), name = 'nova'),
    path('editar/<pk>', ProdutoUpdateView.as_view(), name = 'editar'),
    path('exluir/<pk>', ProdutoDeleteView.as_view(), name = 'excluir'),
]

from django.urls import path
from app.processamento.views import \
    RegraCreateView, RegraUpdateView, RegraDeleteView

app_name = 'processamento'

urlpatterns = [
    path('nova', RegraCreateView.as_view(), name = 'nova'),
    path('editar/<pk>', RegraUpdateView.as_view(), name = 'editar'),
    path('exluir/<pk>', RegraDeleteView.as_view(), name = 'excluir'),

]

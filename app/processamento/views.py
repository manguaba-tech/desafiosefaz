from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from app.processamento.forms import RegrasCreationModelForm
from app.processamento.models import Regra, Classificacao
from app.processamento.serializers import ClassificacaoSerializer


class RegraCreateView(CreateView):
    template_name = 'processamento/regras_formulario.html'
    form_class = RegrasCreationModelForm
    success_url = '/regra/nova'

class RegraUpdateView(UpdateView):
    model = Regra
    template_name = 'processamento/regras_formulario.html'
    form_class = RegrasCreationModelForm
    success_url = '/regra/nova'

class RegraDeleteView(DeleteView):
    model = Regra
    template_name = 'processamento/regras_formulario.html'
    form_class = RegrasCreationModelForm
    success_url = '/regra/nova'

class ClassificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
from django.forms import ModelForm
from app.processamento.models import Regra

class RegrasCreationModelForm(ModelForm):

    class Meta:
        model = Regra
        fields = '__all__'

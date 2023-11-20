from django import forms
from .models import Locality

class LocalityForm(forms.ModelForm):
    class Meta:
        model = Locality
        fields = ['name', 'municipality']
        help_texts = {
            'name': 'Nombre de la localidad',
            'municipality': 'Municipio al que pertenece',
        }
        error_messages = {
            'name': {
                'max_length': 'El nombre es muy largo',
            },
            'municipality': {
                'required': 'El municipio es requerido',
            },
        }
        labels = {
            'name': 'Nombre',
            'municipality': 'Municipio',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control' , 'id' :'name'}),
            'municipality': forms.Select(attrs={'class':'form-control', 'id' : 'municipality' }),
        }

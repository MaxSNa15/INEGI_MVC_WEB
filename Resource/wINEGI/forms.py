from django import forms
from .models import Locality, Residence, Resident, EconomicActivity

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

class ResidenceForm(forms.ModelForm):
    class Meta:
        model = Residence
        fields = ['adress', 'type_of_residence', 'locality']
        help_texts = {
            'adress': 'Dirección de la vivienda',
            'type_of_residence': 'Tipo de vivienda',
            'locality': 'Localidad a la que pertenece',
        }
        error_messages = {
            'adress': {
                'max_length': 'La dirección es muy larga',
            },
            'type_of_residence': {
                'required': 'El tipo de vivienda es requerido',
            },
            'locality': {
                'required': 'La localidad es requerida',
            },
        }
        labels = {
            'adress': 'Dirección',
            'type_of_residence': 'Tipo de vivienda',
            'locality': 'Localidad',
        }
        widgets = {
            'adress': forms.TextInput(attrs={'class':'form-control' , 'id' :'adress'}),
            'type_of_residence': forms.Select(attrs={'class':'form-control', 'id' : 'type_of_residence' }),
            'locality': forms.Select(attrs={'class':'form-control', 'id' : 'locality' }),
        }

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'age', 'birthdate', 'gender', 'residence']
        help_texts = {
            'first_name': 'Nombre del residente',
            'last_name': 'Apellido del residente',
            'age': 'Edad del residente',
            'birthdate': 'Fecha de nacimiento del residente',
            'gender': 'Género del residente',
            'residence': 'Vivienda del residente',
        }
        error_class = {
            'first_name': {
                'max_length': 'El nombre es muy largo',
            },
            'last_name': {
                'max_length': 'El apellido es muy largo',
            },
            'age': {
                'required': 'La edad es requerida',
            },
            'birthdate': {
                'required': 'La fecha de nacimiento es requerida',
            },
            'gender': {
                'required': 'El género es requerido',
            },
            'residence': {
                'required': 'La vivienda es requerida',
            },
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'age': 'Edad',
            'birthdate': 'Fecha de nacimiento',
            'gender': 'Género',
            'residence': 'Vivienda',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control' , 'id' :'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control' , 'id' :'last_name'}),
            'age': forms.NumberInput(attrs={'class':'form-control' , 'id' :'age'}),
            'birthdate': forms.DateInput(attrs={'class':'form-control' , 'id' :'birthdate'}),
            'gender': forms.Select(attrs={'class':'form-control', 'id' : 'gender' }),
            'residence': forms.Select(attrs={'class':'form-control', 'id' : 'residence' }),
        }

class EconomicActivityForm(forms.ModelForm):
    class Meta:
        model = EconomicActivity
        fields = ['name', 'description', 'residence']
        help_texts = {
            'name': 'Nombre de la actividad económica',
            'description': 'Descripción de la actividad económica',
            'residence': 'Vivienda a la que pertenece',
        }
        error_messages = {
            'name': {
                'max_length': 'El nombre es muy largo',
            },
            'description': {
                'max_length': 'La descripción es muy larga',
            },
            'residence': {
                'required': 'La vivienda es requerida',
            },
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'residence': 'Vivienda',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control' , 'id' :'name'}),
            'description': forms.TextInput(attrs={'class':'form-control' , 'id' :'description'}),
            'residence': forms.Select(attrs={'class':'form-control', 'id' : 'residence' }),
        }
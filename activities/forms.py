# -*- coding: utf-8 -*-
from django import forms
from .models import Activities
from country.models import *

class VerifySignUpForm(forms.ModelForm):

    activities = forms.ModelChoiceField(queryset=Activities.objects.filter(active=True),empty_label="por favor seleccione una opcion",widget=forms.Select(attrs={'class':'form-control'}))
    municipios = forms.ModelChoiceField(queryset=section.objects.filter(active=True,fk_section_type_code = 'ad956f07-a5ec-4b57-a3a0-24b3836f75c7'),empty_label="por favor seleccione una opcion",widget=forms.Select(attrs={'class':'form-control', 'onchange':'loadRoom()'}))


    class Meta:
        model = Activities
        fields = '__all__'

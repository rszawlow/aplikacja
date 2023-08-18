from django import forms
from .models import ObiadChoice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ObiadChoiceForm(forms.ModelForm):
    class Meta:
        model = ObiadChoice
        fields = ['want_obiad']

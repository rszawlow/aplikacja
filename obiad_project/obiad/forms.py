from django import forms
from .models import MealChoice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Podaj swoje imię.')
    surname = forms.CharField(max_length=30, required=True, help_text='Podaj swoje nazwisko.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'surname')


class MealChoiceForm(forms.ModelForm):
    class Meta:
        model = MealChoice
        fields = ['want_obiad','want_sniadanie','want_kolacja', 'date']  

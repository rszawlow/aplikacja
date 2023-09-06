from django import forms
from .models import MealChoice
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Podaj swoje imię.')
    surname = forms.CharField(max_length=30, required=True, help_text='Podaj swoje nazwisko.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'surname')






class MealChoiceForm(forms.ModelForm):
    class Meta:
        model = MealChoice
        fields = ['data', 'sniadanie', 'obiad', 'kolacja']
    def __init__(self, *args, **kwargs):
        super(MealChoiceForm, self).__init__(*args, **kwargs)
        self.fields['sniadanie'].widget.attrs['class'] = 'meal-checkbox'
        self.fields['obiad'].widget.attrs['class'] = 'meal-checkbox'
        self.fields['kolacja'].widget.attrs['class'] = 'meal-checkbox'
from django import forms
from .models import MealChoice

class MealChoiceForm(forms.ModelForm):
    class Meta:
        model = MealChoice
        fields = ['want_obiad','want_sniadanie','want_kolacja', 'date']  

from django.contrib import admin
from .models import MealChoice



class MealChoiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'data', 'sniadanie', 'obiad', 'kolacja']
    list_filter = ['user', 'data']


admin.site.register(MealChoice, MealChoiceAdmin)


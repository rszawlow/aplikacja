from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'obiad'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('obiad_choice/', login_required(views.meal_choice), name='obiad_choice'),
    path('kucharz_dashboard/', views.kucharz_dashboard, name='kucharz_dashboard'),
]


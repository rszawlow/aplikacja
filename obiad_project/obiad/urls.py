from django.urls import path
from . import views

app_name = 'obiad'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('obiad_choice/', views.obiad_choice, name='obiad_choice'),
]

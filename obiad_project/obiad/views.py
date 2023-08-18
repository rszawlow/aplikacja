from multiprocessing import AuthenticationError
from django.http import HttpResponseRedirect
from .models import MealChoice
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from .forms import MealChoiceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Konto zostało pomyślnie zarejestrowane. Możesz teraz się zalogować.')
            return redirect('obiad:user_login')
    else:
        form = UserCreationForm()
    return render(request, 'obiad/register.html', {'form': form})


#def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('obiad:obiad_choice')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')
    return render(request, 'obiad/user_login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('obiad:obiad_choice')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.', extra_tags='login_error')
    return render(request, 'obiad/user_login.html')



def index(request):
    return render(request, 'obiad/index.html')



import datetime

@login_required
def meal_choice(request):
    user = request.user
    meal_choice, created = MealChoice.objects.get_or_create(user=user)

    now = datetime.datetime.now()
    current_time = now.time()

    next_choice_date = now.date()

    # Ograniczenia czasowe dla wszystkich dni tygodnia
    if current_time > datetime.time(8, 0):
        next_choice_date += datetime.timedelta(days=1)

    all_days = [(next_choice_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d %A') for i in range(14)]

    if request.method == 'POST':
        form = MealChoiceForm(request.POST, instance=meal_choice)
        if form.is_valid():
            form.save()
            meal_choice.last_choice_date = next_choice_date
            meal_choice.save()
            return redirect('obiad:obiad_choice')
    else:
        form = MealChoiceForm(instance=meal_choice)
    
    return render(request, 'obiad/obiad_choice.html', {'obiad_choice': meal_choice, 'form': form, 'next_choice_date': next_choice_date, 'all_days': all_days})


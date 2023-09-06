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
from .forms import CustomUserCreationForm
import locale
from django.contrib.auth.decorators import user_passes_test

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('obiad:user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'obiad/register.html', {'form': form})


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
    now = datetime.datetime.now()
    start_date = now.date()
    


    if now.time() > datetime.time(8, 0):
        # Jeśli jest po godzinie 8, dodaj jeden dzień do daty początkowej
        start_date += datetime.timedelta(days=1)

    dates = [start_date + datetime.timedelta(days=i) for i in range(14)]
    #user_choices = MealChoice.objects.filter(user=request.user, data__in=dates)
    #print(user_choices)
    if request.method == 'POST':
        form = MealChoiceForm(request.POST)
        if form.is_valid():
            meal_choice = form.save(commit=False)
            meal_choice.user = request.user
            meal_choice.save()
            success_message = "Wybory zostały zapisane pomyślnie."
            return redirect('obiad:obiad_choice')
    else:
        form = MealChoiceForm()
    
    return render(request, 'obiad/obiad_choice.html', {'form': form, 'dates': dates})
'''
def meal_choice(request):
    user = request.user
    
    try:
        meal_choice = MealChoice.objects.get(user=user)
    except MealChoice.DoesNotExist:
        meal_choice = None

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
            if meal_choice is None:
                meal_choice = form.save(commit=False)
                meal_choice.user = user

            for day in all_days:
                want_obiad_key = 'want_obiad_' + day
                want_sniadanie_key = 'want_sniadanie_' + day
                want_kolacja_key = 'want_kolacja_' + day
                meal_choice.want_obiad = request.POST.get(want_obiad_key) == 'on'
                meal_choice.want_sniadanie = request.POST.get(want_sniadanie_key) == 'on'
                meal_choice.want_kolacja = request.POST.get(want_kolacja_key) == 'on'

            meal_choice.last_choice_date = next_choice_date
            meal_choice.save()
            return redirect('obiad:obiad_choice')
    else:
        if meal_choice is None:
            meal_choice = MealChoice(user=user)
        form = MealChoiceForm(instance=meal_choice)

    wybory_uzytkownika = {
        'want_obiad': meal_choice.want_obiad,
        'want_sniadanie': meal_choice.want_sniadanie,
        'want_kolacja': meal_choice.want_kolacja,
    }

    return render(request, 'obiad/obiad_choice.html', {'obiad_choice': meal_choice, 'form': form, 'next_choice_date': next_choice_date, 'all_days': all_days})
'''
@user_passes_test(lambda user: user.groups.filter(name='kucharz').exists())
def kucharz_dashboard(request):
    meal_choices = MealChoice.objects.all()  # Pobierz wszystkie wybory posiłków

    context = {
        'meal_choices': meal_choices,
    }

    return render(request, 'obiad/kucharz_dashboard.html', context)

from django.http import HttpResponse



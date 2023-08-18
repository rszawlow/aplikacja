from multiprocessing import AuthenticationError
from django.http import HttpResponseRedirect
from .models import ObiadChoice
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from .forms import ObiadChoiceForm
from django.contrib import messages

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



def obiad_choice(request):
    user = request.user
    obiad_choice, created = ObiadChoice.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ObiadChoiceForm(request.POST, instance=obiad_choice)
        if form.is_valid():
            form.save()
    else:
        form = ObiadChoiceForm(instance=obiad_choice)

    context = {'form': form}
    return render(request, 'obiad/obiad_choice.html', context)

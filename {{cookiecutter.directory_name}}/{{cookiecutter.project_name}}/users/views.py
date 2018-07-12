from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        pass
    return HttpResponseRedirect('/login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)

            return HttpResponseRedirect('/')
        return render(request, 'users/register.jinja2', {'form': form})
    else:
        return render(request, 'users/register.jinja2', {'form': RegisterForm()})

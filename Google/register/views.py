from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from register.models import Profile


class Register(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'register.html', {'form': form})


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class UsernamesAjax(View):
    def post(self, request):
        form = UserCreationForm(request.POST)

        username = form.cleaned_data.get("username")

        exists = User.objects.filter(username=username).exists()

        return JsonResponse({'exists': username})




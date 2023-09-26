from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm, MyUserCreationForm
from .database import *


def home_page(request):
    title = 'HammerSite'

    context = {'title': title}
    return render(request, 'main/home.html', context)


def sign_in_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {'username': 'username', 'password': 'password', 'page': page}
    return render(request, 'main/sign-in.html', context)


def sign_up_page(request):
    page = 'register'
    if request.user.is_authenticated:
        return redirect('home')

    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'main/sign-up.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def user_profile(request):
    title = 'User Profile'

    context = {'title': title}
    return render(request, 'main/user-profile.html', context)


@login_required(login_url='login')
def user_profile_settings(request):
    title = 'User Profile Settings'

    context = {'title': title}
    return render(request, 'main/user-profile-settings.html', context)


@login_required(login_url='login')
def user_account_settings(request):
    title = 'User Account Settings'
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', user_id=user.id)
        else:
            messages.error(request, 'An error has occurred during update')

    context = {'title': title, 'form': form}
    return render(request, 'main/user-account-settings.html', context)


def other(request):
    context = {}
    return render(request, 'main/!usefull-htmls.html', context)


def list_items(request):
    page = 'items'

    items = db_weapons

    context = {'page': page, 'items': items}
    return render(request, 'main/list.html', context)


def item(request, item_name):
    page = 'item'
    item = db_weapons[item_name]

    context = {'page': page, 'item': item}
    return render(request, 'main/item.html', context)
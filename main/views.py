from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, Item, QualityFlaw
from .tables import ItemTable, QualityFlawTable
from .forms import UserForm, MyUserCreationForm
from .filters import ItemFilter, QualityFlawFilter
from itertools import chain
from django_tables2 import SingleTableView


class ItemListView(SingleTableView):
    table_class = ItemTable
    queryset = Item.objects.all()
    template_name = 'main/items/item_list.html'


class QualityFlawListView(SingleTableView):
    table_class = QualityFlawTable
    queryset = QualityFlaw.objects.all()
    template_name = 'main/qualities/quality_flaw_list.html'


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


def list_items(request):
    order_by = request.GET.get('order_by', 'name')
    sort = request.GET.get('sort', 'descending')

    if sort == 'ascending':
        items_filter = ItemFilter(request.GET, queryset=Item.objects.all())
        items = items_filter.qs.order_by('-' + order_by)
    else:
        items_filter = ItemFilter(request.GET, queryset=Item.objects.all())
        items = items_filter.qs.order_by(order_by)

    context = {'items': items, 'filter': items_filter, 'order_by': order_by, 'sort': sort}
    return render(request, 'main/items/item_list.html', context)


def item(request, id):
    item = Item.objects.get(id=id)
    price = item.price.split(',')

    context = {'item': item, 'price': price}
    return render(request, 'main/items/item.html', context)


def list_qualities_flaws(request):
    order_by = request.GET.get('order_by', 'name')
    sort = request.GET.get('sort', 'descending')

    if sort == 'ascending':
        qualities_flaws_filter = QualityFlawFilter(request.GET, queryset=QualityFlaw.objects.all())
        qualities_flaws = qualities_flaws_filter.qs.order_by('-' + order_by)
    else:
        qualities_flaws_filter = QualityFlawFilter(request.GET, queryset=QualityFlaw.objects.all())
        qualities_flaws = qualities_flaws_filter.qs.order_by(order_by)

    context = {'qualities_flaws': qualities_flaws, 'filter': qualities_flaws_filter, 'order_by': order_by, 'sort': sort}
    return render(request, 'main/qualities/qualities_flaws_list.html', context)


def qualities_flaws(request, id):
    qualities_flaws = QualityFlaw.objects.get(id=id)

    context = {'qualities_flaws': qualities_flaws}
    return render(request, 'main/qualities/qualities_flaws.html', context)

def create_character(request):
    title = 'Create Character'

    context = {'title': title}
    return render(request, 'main/character/create_character.html', context)
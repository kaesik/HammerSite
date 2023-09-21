from django.shortcuts import render

# Create your views here.

def home_page(request):
    title = 'HammerSite'
    context = {'title': title}
    return render(request, 'main/home.html', context)

def sign_in(request):
    context = {}
    return render(request, 'main/sign-in.html', context)

def user_profile(request):
    title = 'User Profile'
    context = {'title': title}
    return render(request, 'main/user-profile.html', context)

def user_profile_settings(request):
    title = 'User Profile Settings'
    context = {'title': title}
    return render(request, 'main/user-profile-settings.html', context)

def user_account_settings(request):
    title = 'User Account Settings'
    context = {'title': title}
    return render(request, 'main/user-account-settings.html', context)
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('sign-in/', views.sign_in, name='sign-in'),

    path('user-profile/', views.user_profile, name='user-profile'),
    path('user-profile-settings/', views.user_profile_settings, name='user-profile-settings'),
    path('user-account-settings/', views.user_account_settings, name='user-account-settings'),
]

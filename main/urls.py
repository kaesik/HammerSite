from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),

    path('sign-in/', views.sign_in_page, name='sign-in'),
    path('sign-up/', views.sign_up_page, name='sign-up'),
    path('logout/', views.logout_user, name='logout'),


    path('user-profile/', views.user_profile, name='user-profile'),
    path('user-profile-settings/', views.user_profile_settings, name='user-profile-settings'),
    path('user-account-settings/', views.user_account_settings, name='user-account-settings'),

    path('list/items/', views.list_items, name='list-items'),
    path('list/items/?<str:id>', views.item, name='item'),
    path('item-list/', views.ItemListView.as_view(), name='item-list'),
]

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login-user'
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'panel/', 
        views.Panel.as_view(), 
        name='user-panel'
    ),
    path(
        'add/', 
        views.PersonaCreateView.as_view(), 
        name='user-panel'
    ),
    path(
        'lista/', 
        views.PersonaListView.as_view(), 
        name='lista'
    ),
]
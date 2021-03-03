"""Workshop URL Configuration."""

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/<str:workshop_slug>/<str:pricing_slug>', views.register,
         name='register'),
    # path('login/', auth_views.LoginView, name='login'),
    path('settings', views.profile_settings, name='profile'),
    path('password', views.profile_password, name='password'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView, name='logout'),
    path('acces_denied/', views.access_denied, name='access_denied'),
]

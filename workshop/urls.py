"""Workshop URL Configuration."""

from django.urls import path
from . import views

app_name = 'workshop'

urlpatterns = [
    # Home Page
    path('<int:year>', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

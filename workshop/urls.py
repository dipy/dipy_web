"""Workshop URL Configuration."""

from django.urls import path
from . import views

app_name = 'workshop'

urlpatterns = [
    # Home Page
    path('<str:workshop_slug>', views.index, name='index'),
    path('w_static/<str:year>', views.index_static, name='index_static'),
    path('eventspace/<str:workshop_slug>', views.eventspace, name='eventspace'),
]

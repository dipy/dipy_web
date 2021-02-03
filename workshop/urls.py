"""Workshop URL Configuration."""

from django.urls import path
from . import views

app_name = 'workshop'

urlpatterns = [
    # Home Page
    path('<str:workshop_id>', views.index, name='index'),
    path('w_static/<str:year>', views.index_static, name='index_static'),
    path('eventspace/', views.eventspace, name='eventspace'),
]

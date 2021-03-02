"""Workshop URL Configuration."""

from django.urls import path
from . import views

app_name = 'workshop'

urlpatterns = [
    # Home Page
    path('courses', views.courses_overview, name='courses'),
    path('w_static/<str:year>', views.index_static, name='index_static'),
    path('eventspace/<str:workshop_slug>', views.eventspace, name='eventspace'),
    path('eventspace/<str:workshop_slug>/calendar', views.eventspace_calendar, name='eventspace_calendar'),
    path('eventspace/<str:workshop_slug>/courses', views.eventspace_courses, name='eventspace_courses'),
    path('eventspace/<str:workshop_slug>/chat', views.eventspace_chat, name='eventspace_chat'),
    path('eventspace/<str:workshop_slug>/sponsor', views.eventspace_sponsor, name='eventspace_sponsor'),
    # path('eventspace/<str:workshop_slug>/help', views.eventspace_help, name='eventspace_help'),
    path('<str:workshop_slug>', views.index, name='index'),
]

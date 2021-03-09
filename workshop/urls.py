"""Workshop URL Configuration."""

from django.urls import path, re_path
from . import views

app_name = 'workshop'

urlpatterns = [
    # Worskhop Management
    path('dashboard/', views.dashboard_workshops,
         name='dashboard_workshops'),
    path('dashboard/add/', views.add_workshop,
         name='add_workshop'),
    re_path(r'^dashboard/edit/(?P<workshop_id>.*?)/$',
            views.edit_workshop, name='edit_workshop'),
    re_path(r'^dashboard/delete/(?P<workshop_id>.*?)/$',
            views.delete_workshop, name='delete_workshop'),
    path('list', views.workshop_list, name='workshop_list'),
    path('w_static/<str:year>', views.index_static, name='index_static'),
    path('eventspace/<str:workshop_slug>', views.eventspace,
         name='eventspace'),
    path('eventspace/<str:workshop_slug>/calendar', views.eventspace_calendar,
         name='eventspace_calendar'),
    path('eventspace/<str:workshop_slug>/calendar/<int:date>',
         views.eventspace_daily, name='eventspace_daily'),
    path('eventspace/<str:workshop_slug>/courses', views.eventspace_courses,
         name='eventspace_courses'),
    path('eventspace/<str:workshop_slug>/courses/<str:lesson_slug>/<str:video_slug>',
         views.eventspace_lesson, name='eventspace_lesson'),
    path('eventspace/<str:workshop_slug>/chat', views.eventspace_chat,
         name='eventspace_chat'),
    path('eventspace/<str:workshop_slug>/sponsor', views.eventspace_sponsor,
         name='eventspace_sponsor'),
    # path('eventspace/<str:workshop_slug>/help', views.eventspace_help,
    #      name='eventspace_help'),
    path('<str:workshop_slug>', views.index, name='index'),
]

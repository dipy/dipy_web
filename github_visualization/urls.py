"""Github Stats URL Configuration."""

from django.urls import path
from . import views

app_name = 'github_visualization'

urlpatterns = [
    # Home Page
    path('', views.github_stats_visualization, name='gh_stats_visualization'),
]

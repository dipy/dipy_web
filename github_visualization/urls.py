from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Home Page
    url(r'^githubstats/$', views.github_stats_visualization,
        name='github_stats_visualization'),

]

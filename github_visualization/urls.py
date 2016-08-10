from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Home Page
    url(r'^contributors$', views.contributors_bubble,
        name='contributors_bubble'),

]

from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Admin Panel Dash Board
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # Admin Panel Login Page
    url(r'^dashboard/login/?$', views.dashboard_login, name='dashboard_login'),

    # Section Management
    url(r'^dashboard/sections/$', views.dashboard_sections,
        name='dashboard_sections'),
    url(r'^dashboard/sections/edit/(?P<position_id>.*?)/$',
        views.edit_website_section, name='edit_website_section'),
    url(r'^dashboard/sections/add/$', views.add_website_section,
        name='add_website_section'),

    # News Management
    url(r'^dashboard/news/$', views.dashboard_news, name='dashboard_news'),
    url(r'^dashboard/news/edit/(?P<news_id>.*?)/$',
        views.edit_news_post, name='edit_news_post'),
    url(r'^dashboard/news/add/$', views.add_news_post,
        name='add_news_post'),


    url('', include('social.apps.django_app.urls', namespace='social')),

]

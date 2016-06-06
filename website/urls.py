from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Cite Page for publications
    url(r'^cite/$', views.cite, name='cite'),

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

    # Publication Management
    url(r'^dashboard/publications/$', views.dashboard_publications,
        name='dashboard_publications'),
    url(r'^dashboard/publications/edit/(?P<publication_id>.*?)/$',
        views.edit_publication, name='edit_publication'),
    url(r'^dashboard/publications/add/(?P<method>.*?)/$',
        views.add_publication, name='add_publication'),

    # social login urls
    url('', include('social.apps.django_app.urls', namespace='social')),

]

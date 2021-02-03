"""Workshop URL Configuration."""

from django.urls import reverse_lazy, path, re_path
from . import views

app_name = 'website'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Section Page
    re_path(r'^page/(?P<position_id>.*?)/$', views.page,
            name='section_page'),

    # Cite Page for publications
    path('cite/', views.cite, name='cite'),

    # News Post display page
    re_path(r'^news/(?P<news_id>.*?)/$', views.news_page, name='news_page'),

    # Honeycomb gallery
    path('gallery/', views.honeycomb, name='gallery'),

    # Tutorials page
    path('tutorials/', views.tutorials, name='tutorials'),

    # Support Page
    path('support/', views.support, name='support'),

    # Follow us page for social feeds
    path('follow/', views.follow_us, name='follow_us'),

    # Contributors page for github stats
    path('contributors/', views.contributors, name='contributors'),

    # Admin Panel Dash Board
    path('dashboard/', views.dashboard, name='dashboard'),

    # Admin Panel Login Page
    path('dashboard/login/', views.dashboard_login, name='dashboard_login'),

    # logout url
    path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),

    # Documentation Pages
    re_path(r'^documentation/latest/(?P<path>.*?)/$',
            views.latest_documentation, name='latest_documentation'),

    re_path(r'^documentation/(?P<version>.*?)/(?P<path>.*?)/$',
            views.documentation, name='documentation'),

    # Section and Page Management
    re_path(r'^dashboard/sections/edit/(?P<section_type_requested>.*?)/(?P<position_id>.*?)/$',
            views.edit_website_section, name='edit_website_section'),
    re_path(r'^dashboard/sections/add/$',
            views.add_website_page, name='add_website_page'),
    re_path(r'^dashboard/sections/delete/(?P<position_id>.*?)/$',
            views.delete_website_page, name='delete_website_page'),
    re_path(r'^dashboard/sections/(?P<section_type_requested>.*?)/$',
            views.dashboard_sections, name='dashboard_sections'),

    # News Management
    path('dashboard/news/', views.dashboard_news, name='dashboard_news'),
    re_path(r'^dashboard/news/edit/(?P<news_id>.*?)/$',
            views.edit_news_post, name='edit_news_post'),
    re_path(r'^dashboard/news/add/$', views.add_news_post,
            name='add_news_post'),
    re_path(r'^dashboard/news/delete/(?P<news_id>.*?)/$',
            views.delete_news_post, name='delete_news_post'),

    # Publication Management
    path('dashboard/publications/', views.dashboard_publications,
         name='dashboard_publications'),
    re_path(r'^dashboard/publications/edit/(?P<publication_id>.*?)/$',
            views.edit_publication, name='edit_publication'),
    re_path(r'^dashboard/publications/add/(?P<method>.*?)/$',
            views.add_publication, name='add_publication'),
    re_path(r'^dashboard/publications/delete/(?P<publication_id>.*?)/$',
            views.delete_publication, name='delete_publication'),
    path('dashboard/publications/highlight/',
         views.highlight_publications, name='highlight_publications'),

    # Carousel Management
    path('dashboard/carousel/', views.dashboard_carousel,
         name='dashboard_carousel'),
    re_path(r'^dashboard/carousel/edit/(?P<carousel_image_id>.*?)/$',
            views.edit_carousel_image, name='edit_carousel_image'),
    path('dashboard/carousel/add/', views.add_carousel_image,
         name='add_carousel_image'),
    re_path(r'^dashboard/carousel/delete/(?P<carousel_image_id>.*?)/$',
            views.delete_carousel_image, name='delete_carousel_image'),

    # sponsor Management
    path('dashboard/sponsor/', views.dashboard_sponsor,
         name='dashboard_sponsor'),
    re_path(r'^dashboard/sponsor/edit/(?P<sponsor_image_id>.*?)/$',
            views.edit_sponsor_image, name='edit_sponsor_image'),
    path('dashboard/sponsor/add/', views.add_sponsor_image,
         name='add_sponsor_image'),
    re_path(r'^dashboard/sponsor/delete/(?P<sponsor_image_id>.*?)/$',
            views.delete_sponsor_image, name='delete_sponsor_image'),

    # Documentation Management
    path('dashboard/documentation/', views.dashboard_documentation,
         name='dashboard_documentation'),
    path('dashboard/documentation/start_update/',
         views.start_update_documentation,
         name='update_documentation'),
    re_path(r'^dashboard/documentation/check_update/(?P<ids>.*?)/$',
            views.check_update_documentation,
            name='check_update_documentation'),

    # Worskhop Management
    path('dashboard/workshops/', views.dashboard_workshops,
         name='dashboard_workshops'),
    path('dashboard/workshops/add/', views.add_workshop,
         name='add_workshop'),
    re_path(r'^dashboard/workshops/edit/(?P<workshop_id>.*?)/$',
            views.edit_workshop, name='edit_workshop'),
    re_path(r'^dashboard/workshops/delete/(?P<workshop_id>.*?)/$',
            views.delete_workshop, name='delete_workshop'),

    # Redirect some Pages
    re_path(r'^reference_cmd/(?P<path>.*?)/$', views.redirect_old_url),
    re_path(r'^reference/(?P<path>.*?)/$', views.redirect_old_url),
    re_path(r'^examples_built/(?P<path>.*?)/$', views.redirect_old_url),
    re_path(r'^examples_index/(?P<path>.*?)/$', views.redirect_old_url),
    re_path(r'^api_changes/(?P<path>.*?)/$', views.redirect_old_url),
    re_path(r'^release_notes/(?P<path>.*?)/$', views.redirect_old_url),
    re_path(r'^(?P<path>.*?)/$', views.redirect_old_url),
]

from django.conf.urls import include, url
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Section Page
    url(r'^page/(?P<position_id>.*?)/$', views.page,
        name='section_page'),

    # Cite Page for publications
    url(r'^cite/$', views.cite, name='cite'),

    # News Post display page
    url(r'^news/(?P<news_id>.*?)/$', views.news_page, name='news_page'),

    # Honeycomb gallery
    url(r'^gallery/$', views.honeycomb, name='gallery'),

    # Tutorials page
    url(r'^tutorials/$', views.tutorials, name='tutorials'),

    # Support Page
    url(r'^support/$', views.support, name='support'),

    # Follow us page for social feeds
    url(r'^follow/$', views.follow_us, name='follow_us'),

    # Admin Panel Dash Board
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # Admin Panel Login Page
    url(r'^dashboard/login/?$', views.dashboard_login, name='dashboard_login'),

    # Documentation Pages
    url(r'^documentation/(?P<version>.*?)/(?P<path>.*?)/$',
        views.documentation, name='documentation'),

    # Section and Page Management
    url(r'^dashboard/sections/edit/(?P<section_type_requested>.*?)/(?P<position_id>.*?)/$',
        views.edit_website_section, name='edit_website_section'),
    url(r'^dashboard/sections/add/$',
        views.add_website_page, name='add_website_page'),
    url(r'^dashboard/sections/delete/(?P<position_id>.*?)/$',
        views.delete_website_page, name='delete_website_page'),
    url(r'^dashboard/sections/(?P<section_type_requested>.*?)/$',
        views.dashboard_sections, name='dashboard_sections'),

    # News Management
    url(r'^dashboard/news/$', views.dashboard_news, name='dashboard_news'),
    url(r'^dashboard/news/edit/(?P<news_id>.*?)/$',
        views.edit_news_post, name='edit_news_post'),
    url(r'^dashboard/news/add/$', views.add_news_post,
        name='add_news_post'),
    url(r'^dashboard/news/delete/(?P<news_id>.*?)/$',
        views.delete_news_post, name='delete_news_post'),

    # Publication Management
    url(r'^dashboard/publications/$', views.dashboard_publications,
        name='dashboard_publications'),
    url(r'^dashboard/publications/edit/(?P<publication_id>.*?)/$',
        views.edit_publication, name='edit_publication'),
    url(r'^dashboard/publications/add/(?P<method>.*?)/$',
        views.add_publication, name='add_publication'),
    url(r'^dashboard/publications/delete/(?P<publication_id>.*?)/$',
        views.delete_publication, name='delete_publication'),
    url(r'^dashboard/publications/highlight/$',
        views.highlight_publications, name='highlight_publications'),

    # Carousel Management
    url(r'^dashboard/carousel/$', views.dashboard_carousel,
        name='dashboard_carousel'),
    url(r'^dashboard/carousel/edit/(?P<carousel_image_id>.*?)/$',
        views.edit_carousel_image, name='edit_carousel_image'),
    url(r'^dashboard/carousel/add/$', views.add_carousel_image,
        name='add_carousel_image'),
    url(r'^dashboard/carousel/delete/(?P<carousel_image_id>.*?)/$',
        views.delete_carousel_image, name='delete_carousel_image'),

    # Honeycomb visualisation Management
    url(r'^dashboard/honeycomb/$', views.dashboard_honeycomb,
        name='dashboard_honeycomb'),
    url(r'^dashboard/honeycomb/edit/(?P<honeycomb_post_id>.*?)/$',
        views.edit_honeycomb_post, name='edit_honeycomb_post'),
    url(r'^dashboard/honeycomb/add/$', views.add_honeycomb_post,
        name='add_honeycomb_post'),
    url(r'^dashboard/honeycomb/delete/(?P<honeycomb_post_id>.*?)/$',
        views.delete_honeycomb_post, name='delete_honeycomb_post'),

    # Documentation Management
    url(r'^dashboard/documentation/$', views.dashboard_documentation,
        name='dashboard_documentation'),
    url(r'^dashboard/documentation/update/$', views.update_documentation,
        name='update_documentation'),

    # social login urls
    url('', include('social.apps.django_app.urls', namespace='social')),

    # logout url
    url(r'^dashboard/logout/$', logout,
        {'next_page': '/'})

]

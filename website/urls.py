from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import logout
from django.views.generic import RedirectView
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

    # Contributors page for github stats
    url(r'^contributors/$', views.contributors, name='contributors'),

    # Admin Panel Dash Board
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # Admin Panel Login Page
    url(r'^dashboard/login/?$', views.dashboard_login, name='dashboard_login'),

    # logout url
    url(r'^dashboard/logout/$', logout,
        {'next_page': reverse_lazy('index')}, name='dashboard_logout'),

    # Documentation Pages
    url(r'^documentation/latest/(?P<path>.*?)/$',
        views.latest_documentation, name='latest_documentation'),

    url(r'^documentation/(?P<version>.*?)/(?P<path>.*?)/$',
        views.documentation, name='documentation'),

    # Redirect some Pages
    url(r'^reference_cmd/(?P<path>.*?)/$', views.redirect_old_url),
    url(r'^reference/(?P<path>.*?)/$', views.redirect_old_url),
    url(r'^examples_built/(?P<path>.*?)/$', views.redirect_old_url),
    url(r'^examples_index/(?P<path>.*?)/$', views.redirect_old_url),
    url(r'^api_changes/(?P<path>.*?)/$', views.redirect_old_url),
    url(r'^release_notes/(?P<path>.*?)/$', views.redirect_old_url),

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

    # sponsor Management
    url(r'^dashboard/sponsor/$', views.dashboard_sponsor,
        name='dashboard_sponsor'),
    url(r'^dashboard/sponsor/edit/(?P<sponsor_image_id>.*?)/$',
        views.edit_sponsor_image, name='edit_sponsor_image'),
    url(r'^dashboard/sponsor/add/$', views.add_sponsor_image,
        name='add_sponsor_image'),
    url(r'^dashboard/sponsor/delete/(?P<sponsor_image_id>.*?)/$',
        views.delete_sponsor_image, name='delete_sponsor_image'),

    # Documentation Management
    url(r'^dashboard/documentation/$', views.dashboard_documentation,
        name='dashboard_documentation'),
    url(r'^dashboard/documentation/start_update/$',
        views.start_update_documentation,
        name='update_documentation'),
    url(r'^dashboard/documentation/check_update/(?P<ids>.*?)/$',
        views.check_update_documentation,
        name='check_update_documentation'),
]

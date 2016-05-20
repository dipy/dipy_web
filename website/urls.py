from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    url(r'^dashboard/editsection/(?P<position_id>.*?)/$',
        views.edit_website_section, name='edit_website_section'),

    url(r'^dashboard/addsection/$', views.add_website_section,
        name='add_website_section'),

    url(r'^dashboard/login/?$', views.dashboard_login, name='dashboard_login'),

    url('', include('social.apps.django_app.urls', namespace='social')),

]

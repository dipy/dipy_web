from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('', include('social.apps.django_app.urls', namespace='social')),

]

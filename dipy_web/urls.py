"""dipy_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = static(settings.MEDIA_URL,
                     document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('admin/', admin.site.urls),
    # social login urls
    path('oauth/', include('social_django.urls', namespace='social')),
    path('users/', include("users.urls", namespace='users')),
    path('githubstats/', include('github_visualization.urls',
                                 namespace='githubstats')),
    path('workshops/', include('workshop.urls', namespace='workshop')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('', include('website.urls')),
]


handler403 = 'website.views.custom403'
handler404 = 'website.views.custom404'
handler500 = 'website.views.custom500'

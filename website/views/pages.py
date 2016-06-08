from django.shortcuts import render
from website.models import *
from django.contrib.auth.decorators import login_required
from .tools import get_website_section, get_latest_news_posts


# Definition of views:

def index(request):
    context = {}
    home_header = get_website_section('home_header')
    getting_started = get_website_section('getting_started')
    latest_news = get_latest_news_posts(5)
    highlighted_publications = Publication.objects.filter(is_highlighted=True)

    context['home_header'] = home_header
    context['getting_started'] = getting_started
    context['latest_news'] = latest_news
    context['highlighted_publications'] = highlighted_publications
    return render(request, 'website/index.html', context)


def cite(request):
    context = {}
    all_publications = Publication.objects.all()
    context['all_publications'] = all_publications
    return render(request, 'website/cite.html', context)


@login_required
def dashboard(request):
        return render(request, 'website/dashboard.html', {})


def dashboard_login(request):
    next_url = request.GET.get('next')
    return render(request, 'website/dashboard_login.html', {'next': next_url})

"""Main pages Management."""

__all__ = ['index', 'page', 'cite', 'honeycomb', 'tutorials', 'support',
           'follow_us', 'news_page', 'contributors', 'dashboard',
           'dashboard_login', 'custom403', 'custom404', 'custom500',
           'redirect_old_url', 'dashboard_logout']

from packaging.version import parse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from .tools import *
from .decorator import github_permission_required
from website.models import *


cache_duration = 15  # cache the view for 30 minutes


@cache_page(60 * cache_duration)
@vary_on_cookie
def index(request):
    context = {}
    doc = DocumentationLink.objects.filter(displayed=True).exclude(version__contains='dev').order_by('-version')
    intro = eval(doc[0].intro) if doc else []

    home_description, announcements, highlights = '', '', ''
    if len(intro) == 3:
        home_description, announcements, highlights = intro[0], intro[1], intro[2]

    # publications = get_dipy_publications()
    latest_news = get_latest_news_posts(5)
    highlighted_publications = Publication.objects.all()[:3]  #.filter(is_highlighted=True)
    all_carousel = CarouselImage.objects.filter(is_visible=True).order_by('-priority')
    all_sponsor = SponsorImage.objects.filter(is_visible=True)

    context['home_description'] = home_description
    context['announcements'] = announcements
    context['highlights'] = highlights
    # context['publications'] = publications
    context['latest_news'] = latest_news
    context['highlighted_publications'] = highlighted_publications
    context['all_carousel'] = all_carousel
    context['all_sponsor'] = all_sponsor
    context['fb_posts'] = get_facebook_page_feed("diffusionimaginginpython", 5)
    context['tweets'] = get_twitter_feed('dipymri', 5)
    context['meta'] = get_meta_tags_dict()

    return render(request, 'website/index.html', context)


def page(request, position_id):
    context = {}
    section = get_website_section(position_id)
    if not section:
        raise Http404("Page does not exist")

    context['section'] = section
    page_title = "DIPY - %s" % (section.title,)
    context['meta'] = get_meta_tags_dict(title=page_title)
    return render(request, 'website/section_page.html', context)


def cite(request):
    context = {}
    all_publications = Publication.objects.all()
    context['all_publications'] = all_publications
    context['meta'] = get_meta_tags_dict(title="DIPY - Publications")
    return render(request, 'website/cite.html', context)


@cache_page(60 * cache_duration)
@vary_on_cookie
def honeycomb(request):
    context = {}
    context['all_youtube_videos'] = get_youtube_videos('UCHnEuCRDGFOR5cfEo0nD3pw', 100)
    doc = DocumentationLink.objects.filter(displayed=True).exclude(version__contains='dev').order_by('-version')
    context['all_documentation_examples'] = eval(doc[0].gallery) if doc else []  # get_doc_examples_images()

    context['meta'] = get_meta_tags_dict(title="DIPY - Gallery")
    return render(request, 'website/honeycomb.html', context)


@cache_page(60 * cache_duration)
@vary_on_cookie
def tutorials(request):
    context = {}
    doc = DocumentationLink.objects.filter(displayed=True).exclude(version__contains='dev').order_by('-version')
    if parse(doc[0].version) >= parse('1.7.0'):
        return redirect('website:documentation', version=doc[0].version,
                        path='examples_built')
    context['all_documentation_examples'] = eval(doc[0].tutorials) if doc else []  # get_doc_examples()
    context['meta'] = get_meta_tags_dict(title="DIPY - Tutorials")
    return render(request, 'website/tutorials.html', context)


def support(request):
    context = {}
    context['meta'] = get_meta_tags_dict(title="DIPY - Support")
    return render(request, 'website/support.html', context)


@cache_page(60 * 5)  # cache the view for 5 minutes
@vary_on_cookie
def follow_us(request):
    context = {}
    context['latest_news'] = get_latest_news_posts(5)
    context['fb_posts'] = get_facebook_page_feed("diffusionimaginginpython", 5)
    context['tweets'] = get_twitter_feed('dipymri', 5)

    context['meta'] = get_meta_tags_dict(title="DIPY - Follow Us")
    return render(request, 'website/follow_us.html', context)


def news_page(request, news_id):
    context = {}
    try:
        news_post = NewsPost.objects.get(id=news_id)
    except ObjectDoesNotExist:
        raise Http404("News Post does not exist")
    context['news_post'] = news_post
    news_title = news_post.title
    meta_title = "DIPY - %s" % (news_title, )
    context['meta'] = get_meta_tags_dict(title=meta_title,
                                         description=news_post.description)
    return render(request, 'website/news.html', context)


@cache_page(60 * cache_duration)
@vary_on_cookie
def contributors(request):
    context = {}
    return render(request, 'website/contributors.html', context)


@login_required
@github_permission_required
def dashboard(request):
    context = {}
    context['meta'] = get_meta_tags_dict()
    return render(request, 'website/dashboard.html', context)


def dashboard_login(request):
    context = {}
    next_url = request.GET.get('next')
    context['next'] = next_url
    context['meta'] = get_meta_tags_dict()
    return render(request, 'website/dashboard_login.html', context)


def dashboard_logout(request):
    logout(request)
    return redirect('website:index')


def custom403(request, exception):
    context = {}
    context['meta'] = get_meta_tags_dict(title="DIPY - 403 Page Not Found")
    return render(request, 'website/error_pages/403.html', context, status=400)


def custom404(request, exception):
    context = {}
    context['meta'] = get_meta_tags_dict(title="DIPY - 404 Page Not Found")
    return render(request, 'website/error_pages/404.html', context, status=400)


def custom500(request):
    context = {}
    context['meta'] = get_meta_tags_dict(title="DIPY - 500 Error Occured")
    return render(request, 'website/error_pages/500.html', context, status=500)


def redirect_old_url(request, path):
    new_path = request.path.replace('.html', '')[1:-1]
    return redirect('website:latest_documentation', path=new_path)

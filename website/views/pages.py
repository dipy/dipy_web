from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from .tools import *
from website.models import *


# Definition of views:
#Temporary disable the cache
# @cache_page(60 * 30)  # cache the view for 30 minutes
def index(request):
    context = {}
    doc = DocumentationLink.objects.filter(displayed=True).exclude(version__contains='dev').order_by('-version')
    intro = eval(doc[0].intro) if doc else []
    if len(intro) == 3:
        home_description, announcements, highlights = intro[0], intro[1], intro[2]
    else:
        home_description, announcements, highlights = '', '', ''
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
    context['workshop_years'] = [2021, 2020, 2019]
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
    context['workshop_years'] = [2021, 2020, 2019]
    page_title = "DIPY - %s" % (section.title,)
    context['meta'] = get_meta_tags_dict(title=page_title)
    return render(request, 'website/section_page.html', context)


def cite(request):
    context = {}
    all_publications = Publication.objects.all()
    context['all_publications'] = all_publications
    context['workshop_years'] = [2021, 2020, 2019]
    context['meta'] = get_meta_tags_dict(title="DIPY - Publications")
    return render(request, 'website/cite.html', context)

#Temporary disable the cache
# @cache_page(60 * 30)  # cache the view for 30 minutes
def honeycomb(request):
    context = {}
    context['all_youtube_videos'] = get_youtube_videos('UCHnEuCRDGFOR5cfEo0nD3pw', 100)
    doc = DocumentationLink.objects.filter(displayed=True).exclude(version__contains='dev').order_by('-version')
    # import ipdb; ipdb.set_trace()
    context['all_documentation_examples'] = eval(doc[0].gallery) if doc else []  # get_doc_examples_images()
    context['workshop_years'] = [2021, 2020, 2019]

    context['meta'] = get_meta_tags_dict(title="DIPY - Gallery")
    return render(request, 'website/honeycomb.html', context)

# Temporary disable the cache
# @cache_page(60 * 30)  # cache the view for 30 minutes
def tutorials(request):
    context = {}
    doc = DocumentationLink.objects.filter(displayed=True).exclude(version__contains='dev').order_by('-version')
    context['all_documentation_examples'] = eval(doc[0].tutorials) if doc else []  # get_doc_examples()
    context['workshop_years'] = [2021, 2020, 2019]
    context['meta'] = get_meta_tags_dict(title="DIPY - Tutorials")
    return render(request, 'website/tutorials.html', context)


def support(request):
    context = {}
    context['workshop_years'] = [2021, 2020, 2019]
    context['meta'] = get_meta_tags_dict(title="DIPY - Support")
    return render(request, 'website/support.html', context)

#Temporary disable the cache
# @cache_page(60 * 5)  # cache the view for 5 minutes
def follow_us(request):
    context = {}
    context['workshop_years'] = [2021, 2020, 2019]
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
    context['workshop_years'] = [2021, 2020, 2019]
    news_title = news_post.title
    meta_title = "DIPY - %s" % (news_title, )
    context['meta'] = get_meta_tags_dict(title=meta_title,
                                         description=news_post.description)
    return render(request, 'website/news.html', context)

#Temporary disable the cache
# @cache_page(60 * 30)  # cache the view for 30 minutes
def contributors(request):
    context = {}
    context['workshop_years'] = [2021, 2020, 2019]
    return render(request, 'website/contributors.html', context)


@login_required
def dashboard(request):
    context = {}
    context['workshop_years'] = [2021, 2020, 2019]
    context['meta'] = get_meta_tags_dict()
    return render(request, 'website/dashboard.html', context)


def dashboard_login(request):
    context = {}
    next_url = request.GET.get('next')
    context['workshop_years'] = [2021, 2020, 2019]
    context['next'] = next_url
    context['meta'] = get_meta_tags_dict()
    return render(request, 'website/dashboard_login.html', context)


def custom404(request, exception):
    context = {}
    context['workshop_years'] = [2021, 2020, 2019]
    context['meta'] = get_meta_tags_dict(title="DIPY - 404 Page Not Found")
    return render(request, 'website/error_pages/404.html', context, status=400)


def custom500(request):
    context = {}
    context['workshop_years'] = [2021, 2020, 2019]
    context['meta'] = get_meta_tags_dict(title="DIPY - 500 Error Occured")
    return render(request, 'website/error_pages/404.html', context, status=400)


def redirect_old_url(request, path):
    new_path = request.path.replace('.html', '')[1:-1]
    return redirect('website:latest_documentation', path=new_path)

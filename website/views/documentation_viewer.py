import os
from bs4 import BeautifulSoup
import requests


from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from django.views.decorators.cache import cache_page

from .tools import get_meta_tags_dict, get_last_release
from workshop.models import Workshop


def latest_documentation(request, path):
    latest_version = get_last_release()
    return redirect('website:documentation', version=latest_version, path=path)


@cache_page(60 * 30)  # cache the view for 30 minutes
def documentation(request, version, path):
    context = {}
    repo_info = (settings.DOCUMENTATION_REPO_OWNER,
                 settings.DOCUMENTATION_REPO_NAME)
    base_url = "https://raw.githubusercontent.com/%s/%s/gh-pages/" % repo_info
    url = base_url + version + "/" + path + ".fjson"
    response = requests.get(url)
    if response.status_code == 404:
        url = base_url + version + "/" + path + "/index.fjson"
        response = requests.get(url)
        if response.status_code == 404:
            url = base_url + version + "/" + path
            response = requests.get(url)
            if response.status_code == 404:
                raise Http404("Page not found")
            else:
                django_response = HttpResponse(
                    content=response.content,
                    status=response.status_code,
                    content_type=response.headers['Content-Type'])
                django_response['Content-Disposition'] = 'inline;'
                django_response['Content-Disposition'] += ' filename=' + os.path.basename(url)
                return django_response

    # parse the content to json
    response_json = response.json()

    response_json['body'] = response_json['body'].replace("¶", "")
    if response_json['parents']:
        if 'documentation' in response_json['parents'][0]['title'].lower():
            response_json['parents'][0]['title'] += ' {}'.format(version)

    if 'documentation' in response_json['title'].lower():
        response_json['title'] += ' {}'.format(version)

    # set title of the json doc as the title of the page
    page_title = "DIPY : Docs %s - %s" % (version,
                                          strip_tags(response_json['title']),)

    context['meta'] = get_meta_tags_dict(title=page_title)

    # try to get first p tag to set as description meta tag
    bs_doc = BeautifulSoup(response_json['body'], 'html.parser')
    first_p = bs_doc.p
    if(first_p):
        first_p_text = first_p.text

        if(len(first_p_text) > 10):
            context['meta'] = get_meta_tags_dict(title=page_title,
                                                 description=first_p_text)

    context['doc'] = response_json
    context['version'] = version
    all_workshops = Workshop.objects.filter(is_published=True).order_by('-start_date')
    context['all_workshops'] = all_workshops
    return render(request, 'website/documentation_page.html', context)

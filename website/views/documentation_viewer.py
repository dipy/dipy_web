from bs4 import BeautifulSoup
import requests


from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.utils.html import strip_tags
from django.views.decorators.cache import cache_page

from .tools import get_meta_tags_dict


@cache_page(60 * 30)  # cache the view for 30 minutes
def documentation(request, version, path):
    context = {}
    repo_info = (settings.DOCUMENTATION_REPO_OWNER,
                 settings.DOCUMENTATION_REPO_NAME)
    base_url = "http://%s.github.io/%s/" % repo_info
    url = base_url + version + "/" + path + ".fjson"
    response = requests.get(url)
    if response.status_code == 404:
        url = base_url + version + "/" + path + "/index.fjson"
        response = requests.get(url)
        if response.status_code == 404:
            raise Http404("Page not found")
    url_dir = url
    if url_dir[-1] != "/":
        url_dir += "/"

    # parse the content to json
    response_json = response.json()

    # replace all image urls to absolute urls
    response_json['body'] = response_json['body'].replace("src=\"",
                                                          "src=\"" + url_dir)

    # try to get first p tag to set as description meta tag
    bs_doc = BeautifulSoup(response_json['body'], 'html.parser')
    first_p_text = bs_doc.p.text

    # set title of the json doc as the title of the page
    page_title = "DIPY : Docs %s - %s" % (version,
                                          strip_tags(response_json['title']),)

    if(len(first_p_text) > 10):
        context['meta'] = get_meta_tags_dict(title=page_title,
                                             description=first_p_text)
    else:
        context['meta'] = get_meta_tags_dict(title=page_title)
    context['doc'] = response_json
    return render(request, 'website/documentation_page.html', context)

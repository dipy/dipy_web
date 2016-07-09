import requests

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page


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
    url_dir = url[:-len(url.split("/")[-1])]
    response_json = response.json()
    response_json['body'] = response_json['body'].replace("src=\"",
                                                          "src=\"" + url_dir)
    context['doc'] = response_json
    return render(request, 'website/documentation_page.html', context)

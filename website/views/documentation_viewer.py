import requests

from django.conf import settings
from django.http import Http404
from django.shortcuts import render


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
    response_json = response.json()
    context['doc'] = response_json
    print(response_json)
    return render(request, 'website/documentation_page.html', context)

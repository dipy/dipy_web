from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
import requests
# Create your views here.


def index(request):
    return HttpResponse('''Hello, world. Welcome to dipy website.''', 200)


@login_required
def dashboard(request):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_website_sections = WebsiteSection.objects.all()
        context = {'all_sections': all_website_sections}
        # if(request.user.has_perm('website.view_section')):
        return render(request, 'website/dashboard.html', context)
    else:
        return render(request, 'website/dashboard.html', {})


def dashboard_login(request):
    next_url = request.GET.get('next')
    return render(request, 'website/dashboard_login.html', {'next': next_url})


# Definition of functons:

def has_commit_permission(access_token, repository_name):
    """
    Determine if user has commit access to the repository in nipy organisation.

    Input
    -----
    access_token : string
        GitHub access token of user.
    repository_name : string
        Name of repository to check if user has commit access to it.
    """
    if access_token == '':
        return False
    response = requests.get('https://api.github.com/orgs/nipy/repos',
                            params={'access_token': access_token})
    response_json = response.json()
    for repo in response_json:
        if(repo["name"] == repository_name):
            permissions = repo["permissions"]
            if(permissions["admin"] and
               permissions["push"] and
               permissions["pull"]):
                return True
    return False

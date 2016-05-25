from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import requests
# Create your views here.


def index(request):
    context = {}
    try:
        home_header = WebsiteSection.objects.get(
            website_position_id="home_header")
    except ObjectDoesNotExist:
        home_header = None

    try:
        getting_started = WebsiteSection.objects.get(
            website_position_id="getting_started")
    except ObjectDoesNotExist:
        getting_started = None

    context['home_header'] = home_header
    context['getting_started'] = getting_started
    return render(request, 'website/index.html', context)


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


@login_required
def edit_website_section(request, position_id):
    # check if user has edit permissions
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    if access_token:
        has_permission = has_commit_permission(access_token, 'dipy_web')
    else:
        has_permission = False

    # if user does not have edit permission:
    if not has_permission:
        return render(request, 'website/editsection.html', {})

    # if user has edit permission:
    try:
        website_section = WebsiteSection.objects.get(
            website_position_id=position_id)
    except:
        raise Http404("Website Section does not exist")

    context = {}
    if request.method == 'POST':
        submitted_form = EditWebsiteSectionForm(request.POST,
                                                instance=website_section)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/')
        else:
            context['website_section'] = website_section
            context['form'] = submitted_form
            return render(request, 'website/editsection.html', context)

    form = EditWebsiteSectionForm(instance=website_section)
    context['website_section'] = website_section
    context['form'] = form
    return render(request, 'website/editsection.html', context)


@login_required
def add_website_section(request):
    # check if user has edit permissions
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    if access_token:
        has_permission = has_commit_permission(access_token, 'dipy_web')
    else:
        has_permission = False

    # if user does not have edit permission:
    if not has_permission:
        return render(request, 'website/addsection.html', {})

    # if user has edit permission:
    context = {}
    if request.method == 'POST':
        submitted_form = AddWebsiteSectionForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addsection.html', context)

    form = AddWebsiteSectionForm()
    context['form'] = form
    return render(request, 'website/addsection.html', context)


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

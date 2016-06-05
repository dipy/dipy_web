from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .tools import has_commit_permission
from website.models import Publication
from website.forms import AddEditPublicationForm
from django.http import Http404


@login_required
def dashboard_publications(request):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_publications = Publication.objects.all()
        context = {'all_publications': all_publications}
        # if(request.user.has_perm('website.view_section')):
        return render(request, 'website/dashboard_publications.html', context)
    else:
        return render(request, 'website/dashboard_publications.html', {})


@login_required
def add_publication(request):
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
        return render(request, 'website/addpublication.html', {})

    # if user has edit permission:
    context = {}
    if request.method == 'POST':
        submitted_form = AddEditPublicationForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/publications/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addpublication.html', context)

    form = AddEditPublicationForm()
    context['form'] = form
    return render(request, 'website/addpublication.html', context)


@login_required
def edit_publication(request, publication_id):
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
        return render(request, 'website/editpublication.html', {})

    # if user has edit permission:
    try:
        publication = Publication.objects.get(
            id=publication_id)
    except:
        raise Http404("Website Section does not exist")

    context = {}
    if request.method == 'POST':
        submitted_form = AddEditPublicationForm(request.POST,
                                                instance=publication)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/publications/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/editpublication.html', context)

    form = AddEditPublicationForm(instance=publication)
    context['form'] = form
    return render(request, 'website/editpublication.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .tools import has_commit_permission
from website.models import WebsiteSection
from website.forms import EditWebsiteSectionForm, AddWebsiteSectionForm
from django.http import Http404


@login_required
def dashboard_sections(request):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_website_sections = WebsiteSection.objects.all()
        context = {'all_sections': all_website_sections}
        return render(request, 'website/dashboard_sections.html', context)
    else:
        return render(request, 'website/dashboard_sections.html', {})


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
            return redirect('/dashboard/sections/')
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
            return redirect('/dashboard/sections/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addsection.html', context)

    form = AddWebsiteSectionForm()
    context['form'] = form
    return render(request, 'website/addsection.html', context)

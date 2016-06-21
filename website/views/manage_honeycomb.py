from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .tools import has_commit_permission
from website.models import HoneycombPost
from website.forms import AddEditHoneycombPostForm
from django.http import Http404


@login_required
def dashboard_honeycomb(request):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_honeycomb_posts = HoneycombPost.objects.all()
        context = {'all_honeycomb_posts': all_honeycomb_posts}
        return render(request, 'website/dashboard_honeycomb.html', context)
    else:
        return render(request, 'website/dashboard_honeycomb.html', {})


@login_required
def add_honeycomb_post(request):
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
        return render(request, 'website/addedithoneycomb.html', {})

    # if user has edit permission:
    context = {}
    if request.method == 'POST':
        submitted_form = AddEditHoneycombPostForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/honeycomb/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addedithoneycomb.html', context)

    form = AddEditHoneycombPostForm()
    context['form'] = form
    return render(request, 'website/addedithoneycomb.html', context)


@login_required
def edit_honeycomb_post(request, honeycomb_post_id):
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
        return render(request, 'website/addedithoneycomb.html', {})

    # if user has edit permission:
    try:
        honeycomb_post = HoneycombPost.get(
            id=honeycomb_post_id)
    except:
        raise Http404("Website Section does not exist")

    context = {}
    if request.method == 'POST':
        submitted_form = AddEditHoneycombPostForm(request.POST,
                                                  instance=honeycomb_post)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/honeycomb/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addedithoneycomb.html', context)

    form = AddEditHoneycombPostForm(instance=honeycomb_post)
    context['form'] = form
    return render(request, 'website/addedithoneycomb.html', context)


@login_required
def delete_honeycomb_post(request, honeycomb_post_id):
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
        return render(request, 'website/addedithoneycomb.html', {})
    try:
        n = HoneycombPost.objects.get(id=honeycomb_post_id)
    except:
        raise Http404("Honeycomb Post does not exist")
    n.delete()
    return redirect('/dashboard/honeycomb/')

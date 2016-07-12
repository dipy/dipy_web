from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, redirect

from .tools import has_commit_permission
from website.forms import AddEditNewsPostForm
from website.models import NewsPost


@login_required
def dashboard_news(request):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_news_posts = NewsPost.objects.all()
        context = {'all_news_posts': all_news_posts}
        return render(request, 'website/dashboard_news.html', context)
    else:
        raise PermissionDenied


@login_required
def add_news_post(request):
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
        raise PermissionDenied

    # if user has edit permission:
    context = {}
    if request.method == 'POST':
        submitted_form = AddEditNewsPostForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/news/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditnews.html', context)

    form = AddEditNewsPostForm()
    context['form'] = form
    return render(request, 'website/addeditnews.html', context)


@login_required
def edit_news_post(request, news_id):
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
        raise PermissionDenied

    # if user has edit permission:
    try:
        news_post = NewsPost.objects.get(
            id=news_id)
    except:
        raise Http404("Website Section does not exist")

    context = {}
    if request.method == 'POST':
        submitted_form = AddEditNewsPostForm(request.POST,
                                             instance=news_post)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/news/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditnews.html', context)

    form = AddEditNewsPostForm(instance=news_post)
    context['form'] = form
    return render(request, 'website/addeditnews.html', context)


@login_required
def delete_news_post(request, news_id):
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
        raise PermissionDenied
    try:
        n = NewsPost.objects.get(id=news_id)
    except:
        raise Http404("Publication does not exist")
    n.delete()
    return redirect('/dashboard/news/')

"""News Management."""

__all__ = ['dashboard_news', 'add_news_post', 'edit_news_post',
           'delete_news_post']

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .decorator import github_permission_required
from website.forms import AddEditNewsPostForm
from website.models import NewsPost


@login_required
@github_permission_required
def dashboard_news(request):
    all_news_posts = NewsPost.objects.all()
    context = {'all_news_posts': all_news_posts}
    return render(request, 'website/dashboard_news.html', context)


@login_required
@github_permission_required
def add_news_post(request):
    context = {'title': 'Add'}
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
@github_permission_required
def edit_news_post(request, news_id):
    try:
        news_post = NewsPost.objects.get(id=news_id)
    except Exception:
        raise Http404("Website Section does not exist")

    context = {'title': 'Edit'}
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
@github_permission_required
def delete_news_post(request, news_id):
    try:
        n = NewsPost.objects.get(id=news_id)
    except Exception:
        raise Http404("Publication does not exist")
    n.delete()
    return redirect('/dashboard/news/')

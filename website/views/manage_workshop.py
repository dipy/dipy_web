"""Workshop Management."""

__all__ = ['dashboard_workshops', 'add_workshop', 'edit_workshop',
           'delete_workshop']

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .decorator import github_permission_required
from website.forms import AddEditNewsPostForm
from workshop.models import Workshop


@login_required
@github_permission_required
def dashboard_workshops(request):
    all_workshop = Workshop.objects.all()
    context = {'all_workshop': all_workshop}
    return render(request, 'website/dashboard_workshops.html', context)


@login_required
@github_permission_required
def add_workshop(request):
    context = {}
    if request.method == 'POST':
        submitted_form = AddEditNewsPostForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/news/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditworkshop.html', context)

    form = AddEditNewsPostForm()
    context['form'] = form
    return render(request, 'website/addeditworkshop.html', context)


@login_required
@github_permission_required
def edit_workshop(request, workshop_id):
    try:
        news_post = Workshop.objects.get(id=workshop_id)
    except Exception:
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
@github_permission_required
def delete_workshop(request, workshop_id):
    try:
        w = Workshop.objects.get(id=workshop_id)
    except Exception:
        raise Http404("Publication does not exist")

    w.delete()
    return redirect('/dashboard/workshops/')

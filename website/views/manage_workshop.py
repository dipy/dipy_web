"""Workshop Management."""

__all__ = ['dashboard_workshops', 'add_workshop', 'edit_workshop',
           'delete_workshop']

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .decorator import github_permission_required
from workshop.forms import AddEditWorkshopForm
from workshop.models import Workshop


@login_required
@github_permission_required
def dashboard_workshops(request):
    all_workshops = Workshop.objects.all()
    context = {'all_workshops': all_workshops}
    return render(request, 'website/dashboard_workshops.html', context)


@login_required
@github_permission_required
def add_workshop(request):
    context = {'title': 'Add'}
    if request.method == 'POST':
        submitted_form = AddEditWorkshopForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/workshops/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditworkshop.html', context)

    form = AddEditWorkshopForm()
    context['form'] = form
    return render(request, 'website/addeditworkshop.html', context)


@login_required
@github_permission_required
def edit_workshop(request, workshop_id):
    try:
        workshop = Workshop.objects.get(id=workshop_id)
    except Exception:
        raise Http404("Workshop does not exist")

    context = {'title': 'Edit'}
    if request.method == 'POST':
        submitted_form = AddEditWorkshopForm(request.POST,
                                             instance=workshop)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/workshops/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditworkshop.html', context)

    form = AddEditWorkshopForm(instance=workshop)
    context['form'] = form
    return render(request, 'website/addeditworkshop.html', context)


@login_required
@github_permission_required
def delete_workshop(request, workshop_id):
    try:
        w = Workshop.objects.get(id=workshop_id)
    except Exception:
        raise Http404("Workshop does not exist")

    w.delete()
    return redirect('/dashboard/workshops/')

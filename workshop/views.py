"""Main Workshop pages Management."""

__all__ = ['index_static', 'index', 'eventspace', 'dashboard_workshops',
           'add_workshop', 'edit_workshop', 'delete_workshop']

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone

from website.views.decorator import github_permission_required

from .models import *
from .forms import AddEditWorkshopForm


def index_static(request, year):
    """Old Workshop index page. Now it is dynamic."""
    return render(request, f'workshop/index_{year}.html', {})


def index(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    if not workshop:
        raise Http404()

    if not workshop.is_published:
        raise Http404()

    context = {}
    context['workshop'] = workshop

    if timezone.now() < workshop.registration_start_date:
        return render(request, 'workshop/comingsoon.html', context)

    context["STRIPE_PUBLIC_KEY"] = settings.STRIPE_PUBLIC_KEY
    return render(request, 'workshop/index.html', context)


@login_required
def courses_overview(request):
    user = request.user
    workshops = user.workshops.all()
    context = {}
    context['all_workshop'] = workshops
    return render(request, 'workshop/eventlist.html', context)


@login_required
def eventspace(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    context = {}
    context['workshop'] = workshop
    return render(request, 'workshop/eventspace.html', context)


@login_required
def eventspace_chat(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    context = {}
    context['workshop'] = workshop
    return render(request, 'workshop/eventspace_chat.html', context)


@login_required
def eventspace_sponsor(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    context = {}
    context['workshop'] = workshop
    return render(request, 'workshop/eventspace_sponsor.html', context)


@login_required
def eventspace_calendar(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    context = {}
    context['workshop'] = workshop
    return render(request, 'workshop/eventspace_calendar.html', context)


@login_required
def eventspace_courses(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    context = {}
    context['workshop'] = workshop
    return render(request, 'workshop/eventspace_courses.html', context)


@login_required
@github_permission_required
def dashboard_workshops(request):
    all_workshops = Workshop.objects.all()
    context = {'all_workshops': all_workshops}
    return render(request, 'workshop/dashboard_workshops.html', context)


@login_required
@github_permission_required
def add_workshop(request):
    context = {'title': 'Add'}
    if request.method == 'POST':
        submitted_form = AddEditWorkshopForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('workshop:dashboard_workshops')
        else:
            context['form'] = submitted_form
            return render(request, 'workshop/addeditworkshop.html', context)

    form = AddEditWorkshopForm()
    context['form'] = form
    return render(request, 'workshop/addeditworkshop.html', context)


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
            return redirect('workshop:dashboard_workshops')
        else:
            context['form'] = submitted_form
            return render(request, 'workshop/addeditworkshop.html', context)

    form = AddEditWorkshopForm(instance=workshop)
    context['form'] = form
    return render(request, 'workshop/addeditworkshop.html', context)


@login_required
@github_permission_required
def delete_workshop(request, workshop_id):
    try:
        w = Workshop.objects.get(id=workshop_id)
    except Exception:
        raise Http404("Workshop does not exist")

    w.delete()
    return redirect('workshop:dashboard_workshops')

"""Main Workshop pages Management."""

__all__ = ['index_static', 'index', 'eventspace', ]

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from .models import *


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



"""Main Workshop pages Management."""

__all__ = ['index_static', 'index', 'eventspace', ]

from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from .models import *


def index_static(request, year):
    """Old Workshop index page. Now it is dynamic."""
    return render(request, f'workshop/index_{year}.html', {})


def index(request, workshop_id):
    workshop = Workshop.objects.filter(id=workshop_id)
    if not workshop or len(workshop) > 1:
        raise Http404()

    workshop = workshop[0]
    if not workshop.is_published:
        raise Http404()

    context = {}
    context['workshop'] = workshop

    if timezone.now() < workshop.registration_start_date:
        return render(request, 'workshop/comingsoon.html', context)

    return render(request, 'workshop/index.html', context)


def eventspace(request):
    context = {}
    return render(request, 'workshop/eventspace.html', context)

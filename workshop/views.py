"""Main Workshop pages Management."""

__all__ = ['index_static', 'index', 'eventspace', 'dashboard_workshops',
           'add_workshop', 'edit_workshop', 'delete_workshop']

import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone

from website.views.decorator import github_permission_required

from .models import *
from .forms import AddEditWorkshopForm
from .tools import get_workshop_tweet


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
def workshop_list(request):
    user = request.user
    workshops = user.workshops.all()
    context = {}
    context['all_workshop'] = workshops
    return render(request, 'workshop/eventlist.html', context)


@login_required
def eventspace(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)

    context = {'workshop': workshop,
               'tweets': get_workshop_tweet(workshop.hashtags())
               }
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
def eventspace_daily(request, workshop_slug, date):
    dt_date = datetime.datetime.strptime(str(date), "%Y%m%d")
    dt_date = timezone.make_aware(dt_date)
    workshop = Workshop.objects.get(slug__contains=workshop_slug)

    all_lesson = Lesson.objects.filter(events__start_date__date=dt_date,
                                       events__workshop=workshop)
    all_qa = QA.objects.filter(events__start_date__date=dt_date,
                               events__workshop=workshop)

    video_id = request.GET.get('video_id', None)
    now = datetime.datetime.now()
    now = now.replace(hour=0, minute=0, second=0, microsecond=0)
    can_release_videos = timezone.make_aware(now) >= dt_date

    # print(now)
    # print(dt_date)
    # print(can_release_videos)

    context = {'workshop': workshop,
               'all_lesson': all_lesson,
               'all_qa': all_qa,
               'release_date': dt_date,
               'can_release_videos': can_release_videos}

    if video_id is not None:
        vid = Video.objects.get(id=video_id)
    else:
        vid = all_lesson[0].videos.first()
    context["video"] = vid

    return render(request, 'workshop/eventspace_daily.html', context)


@login_required
def eventspace_courses(request, workshop_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    all_lesson = Lesson.objects.filter(events__in=workshop.events.all())

    context = {'workshop': workshop,
               'all_lesson': all_lesson,
               }
    return render(request, 'workshop/eventspace_courses.html', context)


@login_required
def eventspace_lesson(request, workshop_slug, lesson_slug, video_slug):
    workshop = Workshop.objects.get(slug__contains=workshop_slug)
    lesson = Lesson.objects.get(slug__contains=lesson_slug)
    video = Video.objects.get(slug__contains=video_slug)

    event = lesson.events.filter(workshop=workshop).last()

    now = datetime.datetime.now()
    now = now.replace(hour=0, minute=0, second=0, microsecond=0)
    can_release_videos = timezone.make_aware(now) >= event.start_date

    # print(video.video_id())
    # print(now)
    # print(event.start_date)
    # print(can_release_videos)

    context = {'workshop': workshop,
               'lesson': lesson,
               'video': video,
               'release_date': event.start_date,
               'can_release_videos': can_release_videos}
    return render(request, 'workshop/eventspace_lesson.html', context)


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

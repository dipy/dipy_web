
from django import template
# from django.conf import settings
from workshop.models import Workshop

register = template.Library()


@register.inclusion_tag('workshop/workshop_menu.html')
def show_workshop_menu():
    all_workshops = Workshop.objects.filter(is_published=True).order_by('-start_date')
    return {'all_workshops': all_workshops}


@register.filter(name='is_lesson')
def is_lesson(track):
    return hasattr(track, 'lesson')


@register.simple_tag(name='qa_time')
def qa_time(qa, workshop):
    t = qa.events.get(workshop=workshop).start_date
    return t.strftime("%H:%M %p")


@register.filter(name='in_workshops')
def in_workshops(things, workshop):
    return things.filter(workshops=workshop)


@register.filter(name='in_workshop')
def in_workshop(things, workshop):
    return things.filter(workshop=workshop)


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

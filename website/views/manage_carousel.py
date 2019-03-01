from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, redirect

from .tools import has_commit_permission
from website.forms import AddEditCarouselImageForm, AddEditSponsorImageForm
from website.models import CarouselImage, SponsorImage


@login_required
def dashboard_sponsor(request):
    return _dashboard_image(request, SponsorImage, 'all_sponsor_images',
                            'website/dashboard_sponsor.html')


@login_required
def dashboard_carousel(request):
    return _dashboard_image(request, CarouselImage, 'all_carousel_images',
                            'website/dashboard_carousel.html')


def _dashboard_image(request, model, model_name, template):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_images = model.objects.all()
        context = {model_name: all_images}
        return render(request, template, context)
    else:
        raise PermissionDenied


@login_required
def add_sponsor_image(request):
    return _add_image(request, AddEditSponsorImageForm, '/sponsor/',
                      'website/addeditsponsor.html')


@login_required
def add_carousel_image(request):
    return _add_image(request, AddEditCarouselImageForm, '/carousel/',
                     'website/addeditcarousel.html')


def _add_image(request, model_form, path, template):
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
        submitted_form = model_form(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard' + path)
        else:
            context['form'] = submitted_form
            return render(request, template, context)

    form = AddEditCarouselImageForm()
    context['form'] = form
    return render(request, template, context)


@login_required
def edit_sponsor_image(request, sponsor_image_id):
    return _edit_image(request, sponsor_image_id, SponsorImage,
                       AddEditSponsorImageForm, '/sponsor/',
                       'website/addeditsponsor.html')


@login_required
def edit_carousel_image(request, carousel_image_id):
    return _edit_image(request, carousel_image_id, CarouselImage,
                       AddEditCarouselImageForm, '/carousel/',
                       'website/addeditcarousel.html')


def _edit_image(request, carousel_image_id, model, model_form, path, template):
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
        carousel_image = model.objects.get(id=carousel_image_id)
    except:
        raise Http404("Website Section does not exist")

    context = {}
    if request.method == 'POST':
        submitted_form = model_form(request.POST, instance=carousel_image)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard' + path)
        else:
            context['form'] = submitted_form
            return render(request, template, context)

    form = AddEditCarouselImageForm(instance=carousel_image)
    context['form'] = form
    return render(request, template, context)


@login_required
def delete_sponsor_image(request, sponsor_image_id):
    return _delete_image(request, sponsor_image_id, SponsorImage,
                         '/sponsor/')


@login_required
def delete_carousel_image(request, carousel_image_id):
    return _delete_image(request, carousel_image_id, CarouselImage,
                         '/carousel/')

def _delete_image(request, carousel_image_id, model, path):
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
        n = model.objects.get(id=carousel_image_id)
    except:
        raise Http404("Carousel Image does not exist")
    n.delete()
    return redirect('/dashboard' + path)

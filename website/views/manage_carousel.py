from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, redirect

from .tools import has_commit_permission
from website.forms import AddEditCarouselImageForm
from website.models import CarouselImage


@login_required
def dashboard_carousel(request):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_carousel_images = CarouselImage.objects.all()
        context = {'all_carousel_images': all_carousel_images}
        return render(request, 'website/dashboard_carousel.html', context)
    else:
        raise PermissionDenied


@login_required
def add_carousel_image(request):
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
        submitted_form = AddEditCarouselImageForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/carousel/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditcarousel.html', context)

    form = AddEditCarouselImageForm()
    context['form'] = form
    return render(request, 'website/addeditcarousel.html', context)


@login_required
def edit_carousel_image(request, carousel_image_id):
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
        carousel_image = CarouselImage.objects.get(
            id=carousel_image_id)
    except:
        raise Http404("Website Section does not exist")

    context = {}
    if request.method == 'POST':
        submitted_form = AddEditCarouselImageForm(request.POST,
                                                  instance=carousel_image)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/carousel/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditcarousel.html', context)

    form = AddEditCarouselImageForm(instance=carousel_image)
    context['form'] = form
    return render(request, 'website/addeditcarousel.html', context)


@login_required
def delete_carousel_image(request, carousel_image_id):
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
        n = CarouselImage.objects.get(id=carousel_image_id)
    except:
        raise Http404("Carousel Image does not exist")
    n.delete()
    return redirect('/dashboard/carousel/')

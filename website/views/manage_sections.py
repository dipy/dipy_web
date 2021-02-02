"""Section Management."""

__all__ = ['dashboard_sections', 'edit_website_section', 'add_website_page',
           'delete_website_page']

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .decorator import github_permission_required
from website.forms import AddEditPageSectionForm, EditFixedSectionForm
from website.models import WebsiteSection


@login_required
@github_permission_required
def dashboard_sections(request, section_type_requested):
    if not (section_type_requested == "page" or
            section_type_requested == "fixed"):
        raise Http404("Page Not Found")

    website_sections = WebsiteSection.objects.filter(
        section_type=section_type_requested)
    context = {'sections': website_sections}
    context["type"] = section_type_requested
    return render(request, 'website/dashboard_sections.html', context)


@login_required
@github_permission_required
def edit_website_section(request, section_type_requested, position_id):
    try:
        section = WebsiteSection.objects.get(
            website_position_id=position_id)
    except Exception:
        raise Http404("Section does not exist")
    if(section.section_type != section_type_requested):
        raise Http404("Section does not exist")

    context = {}
    if request.method == 'POST':
        if(section_type_requested == "page"):
            submitted_form = AddEditPageSectionForm(request.POST,
                                                    instance=section)
        elif(section_type_requested == "fixed"):
            submitted_form = EditFixedSectionForm(request.POST,
                                                  instance=section)
        else:
            raise Http404("Section does not exist")

        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/sections/' + section_type_requested)
        else:
            context['section'] = section
            context['form'] = submitted_form
            return render(request, 'website/editsection.html', context)

    if(section_type_requested == "page"):
        form = AddEditPageSectionForm(instance=section)
    elif(section_type_requested == "fixed"):
        form = EditFixedSectionForm(instance=section)
    else:
        raise Http404("Section does not exist")

    context['section'] = section
    context['form'] = form
    return render(request, 'website/editsection.html', context)


@login_required
@github_permission_required
def add_website_page(request):
    context = {}
    if request.method == 'POST':
        submitted_form = AddEditPageSectionForm(request.POST)
        if submitted_form.is_valid():
            page_section = submitted_form.save(commit=False)
            page_section.section_type = "page"
            page_section.save()
            return redirect('/dashboard/sections/page')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addpagesection.html', context)

    form = AddEditPageSectionForm()
    context['form'] = form
    return render(request, 'website/addpagesection.html', context)


@login_required
@github_permission_required
def delete_website_page(request, position_id):
    try:
        page_section = WebsiteSection.objects.get(
            website_position_id=position_id)
    except Exception:
        raise Http404("Page does not exist")
    if(page_section.section_type == 'page'):
        page_section.delete()
    else:
        raise Http404
    return redirect('/dashboard/sections/page')

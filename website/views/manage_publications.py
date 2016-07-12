import bibtexparser
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, redirect

from .tools import has_commit_permission
from website.forms import AddEditPublicationForm
from website.models import Publication


@login_required
def dashboard_publications(request):
    try:
        social = request.user.social_auth.get(provider='github')
        access_token = social.extra_data['access_token']
    except:
        access_token = ''
    has_permission = has_commit_permission(access_token, 'dipy_web')
    if has_permission:
        all_publications = Publication.objects.all()
        context = {'all_publications': all_publications}
        return render(request, 'website/dashboard_publications.html', context)
    else:
        raise PermissionDenied


@login_required
def add_publication(request, method):
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
    if(method == "manual"):
        context = {}
        if request.method == 'POST':
            submitted_form = AddEditPublicationForm(request.POST)
            if submitted_form.is_valid():
                submitted_form.save()
                return redirect('/dashboard/publications/')
            else:
                context['form'] = submitted_form
                return render(request, 'website/addeditpublication.html',
                              context)

        form = AddEditPublicationForm()
        context['form'] = form
        return render(request, 'website/addeditpublication.html', context)
    elif(method == "bibtex"):
        if request.method == 'POST':
            bibtex_entered = request.POST.get('bibtex')
            try:
                bib_parsed = bibtexparser.loads(bibtex_entered)
                bibInfo = bib_parsed.entries[0]

                if 'title' in bibInfo:
                    title = bibInfo['title']
                else:
                    title = None

                if 'author' in bibInfo:
                    authors = bibInfo['author']
                elif 'authors' in bibInfo:
                    authors = bibInfo['aithors']
                else:
                    authors = None

                if 'url' in bibInfo:
                    url = bibInfo['url']
                elif 'link' in bibInfo:
                    url = bibInfo['link']
                elif 'doi' in bibInfo:
                    url = "http://dx.doi.org/" + bibInfo['doi']
                else:
                    url = None

                if(title and authors and url):
                    publicationObj = Publication(title=title,
                                                 author=authors,
                                                 url=url)
                    if 'ENTRYTYPE' in bibInfo:
                        publicationObj.entry_type = bibInfo['ENTRYTYPE']
                    if 'doi' in bibInfo:
                        publicationObj.doi = bibInfo['doi']
                    if 'journal' in bibInfo:
                        publicationObj.published_in = bibInfo['journal']
                    if 'booktitle' in bibInfo:
                        publicationObj.published_in = bibInfo['booktitle']
                    if 'publisher' in bibInfo:
                        publicationObj.publisher = bibInfo['publisher']
                    if 'year' in bibInfo:
                        publicationObj.year_of_publication = bibInfo['year']
                    if 'month' in bibInfo:
                        publicationObj.month_of_publication = bibInfo['month']
                    publicationObj.bibtex = bibtex_entered
                    publicationObj.save()
                    return redirect('/dashboard/publications/')

                else:
                    return render(request,
                                  'website/addpublicationbibtex.html', {})
            except:
                return render(request, 'website/addpublicationbibtex.html', {})

        else:
            return render(request, 'website/addpublicationbibtex.html', {})
    else:
        raise Http404("Not a valid method for adding publications.")


@login_required
def edit_publication(request, publication_id):
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
        publication = Publication.objects.get(
            id=publication_id)
    except:
        raise Http404("Publication does not exist")

    context = {}
    if request.method == 'POST':
        submitted_form = AddEditPublicationForm(request.POST,
                                                instance=publication)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/dashboard/publications/')
        else:
            context['form'] = submitted_form
            return render(request, 'website/addeditpublication.html', context)

    form = AddEditPublicationForm(instance=publication)
    context['form'] = form
    return render(request, 'website/addeditpublication.html', context)


@login_required
def delete_publication(request, publication_id):
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
        p = Publication.objects.get(id=publication_id)
    except:
        raise Http404("Publication does not exist")
    p.delete()
    return redirect('/dashboard/publications/')


@login_required
def highlight_publications(request):
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
    else:
        if request.method == 'POST':
            highlighted_publications = request.POST.getlist('highlights[]')
            all_publications = Publication.objects.all()

            for p in all_publications:
                if str(p.id) in highlighted_publications:
                    p.is_highlighted = True
                else:
                    p.is_highlighted = False
                p.save()
            return redirect('/dashboard/publications/')
        else:
            all_publications = Publication.objects.all()
            context = {'all_publications': all_publications}
            return render(request, 'website/highlightpublications.html',
                          context)

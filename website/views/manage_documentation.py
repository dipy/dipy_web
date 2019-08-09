from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .tools import update_documentations, has_commit_permission
from website.models import DocumentationLink


def dashboard_documentation(request):
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

    context = {}
    if request.method == 'POST':
        selected_docs = request.POST.getlist('docs[]')
        all_docs = DocumentationLink.objects.all()

        for doc in all_docs:
            if str(doc.id) in selected_docs:
                doc.displayed = True
            else:
                doc.displayed = False
            doc.save()
        return redirect('/dashboard/documentation/')
    else:
        context["all_docs"] = DocumentationLink.objects.all()
        return render(request, 'website/dashboard_documentation.html',
                      context)


def start_update_documentation(request):
    d_ids = update_documentations()
    return JsonResponse(d_ids)


def check_update_documentation(request, ids):
    ids = tuple(map(int, ids.split('_')))
    updated_doc = DocumentationLink.objects.filter(id__in=ids, is_updated=False)
    is_done = False if len(updated_doc) else True
    return JsonResponse({'is_done': is_done})

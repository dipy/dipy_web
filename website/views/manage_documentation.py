"""Documentation Management."""

__all__ = ['dashboard_documentation', 'start_update_documentation',
           'check_update_documentation']

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .tools import update_documentations
from .decorator import github_permission_required
from website.models import DocumentationLink


@login_required
@github_permission_required
def dashboard_documentation(request):
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


@login_required
@github_permission_required
def start_update_documentation(request):
    d_ids = update_documentations()
    return JsonResponse(d_ids)


@login_required
@github_permission_required
def check_update_documentation(request, ids):
    ids = tuple(map(int, ids.split('_')))
    updated_doc = DocumentationLink.objects.filter(id__in=ids,
                                                   is_updated=False)
    is_done = False if len(updated_doc) else True
    return JsonResponse({'is_done': is_done})

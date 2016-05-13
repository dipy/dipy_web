from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


def index(request):
    return HttpResponse('''Hello, world. Welcome to dipy website.''', 200)


@login_required
def dashboard(request):
    all_website_sections = WebsiteSection.objects.all()
    context = {'all_sections': all_website_sections}
    return render(request, 'website/dashboard.html', context)


def dashboard_login(request):
    next_url = request.GET.get('next')
    return render(request, 'website/dashboard_login.html', {'next': next_url})

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return HttpResponse('''Hello, world. Welcome to dipy website.''', 200)


@login_required
def dashboard(request):
    return HttpResponse('''This is your dashboard.
                           You can view this only
                           if you are authenticed''', 200)


def dashboard_login(request):
    next_url = request.GET.get('next')
    return render(request, 'website/dashboard_login.html', {'next': next_url})

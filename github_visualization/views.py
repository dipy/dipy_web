from django.shortcuts import render
from .tools import *


# Create your views here.

def contributors_bubble(request):
    context = {}
    context['contributors'] = fetch_all_contributors('nipy', 'dipy')
    return render(request,
                  'github_visualization/contributors_bubble.html',
                  context)

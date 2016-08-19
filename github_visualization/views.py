from django.shortcuts import render


# Create your views here.

def github_stats_visualization(request):
    context = {}
    return render(request, 'github_visualization/github_stats.html', context)

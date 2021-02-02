from django.shortcuts import render


# Create your views here.
def index(request, year):
    old_page = [2019, 2020]
    if year in old_page:
        return render(request, f'workshop/index_{year}.html', {})

    context = {}
    context['workshop_year'] = year
    return render(request, 'workshop/index.html', context)


def dashboard(request):
    context = {}
    return render(request, 'workshop/dashboard.html', context)

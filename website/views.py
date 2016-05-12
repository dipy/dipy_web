from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('''Hello, world. Welcome to dipy website.''', 200)
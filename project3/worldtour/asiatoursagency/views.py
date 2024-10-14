from django.shortcuts import render
from .models import tour


def index(request):
    tours = tour.objects.all()
    context = {'tours':tours}
    return render(request, 'tours/index.html', context)

def index2(request):
    return render(request, 'django_app/index.html')
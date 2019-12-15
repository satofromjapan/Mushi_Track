from django.shortcuts import render
from django.http import HttpResponse
from .models import Mushi

# Create your views here.
def home(request):
    context = {
        'posts': Mushi.objects.all()
    }
    return render(request, 'tracker/home.html', context)

def about(request):

    return render(request, 'tracker/about.html', {'title': 'About'})
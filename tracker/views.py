from django.shortcuts import render
from django.http import HttpResponse

#dummydata

posts =[
    {
        'author': 'Masato',
        'title': 'Issue 1',
        'content': 'First issue content',
        'date_posted': '12/3/2019'
    },
    {
        'author': 'Masakpo',
        'title': 'Issue 2',
        'content': 'Second issue content',
        'date_posted': '12/4/2019'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'tracker/home.html', context)

def about(request):
    return render(request, 'tracker/about.html')
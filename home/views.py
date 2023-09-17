from django.shortcuts import render
from .models import Solutions, Slides
from .models import Evenement, Galerie
from .models import Blog, Multimedia, About

def index(request):
    solutions = Solutions.objects.all().order_by('-date')
    slides = Slides.objects.all().order_by('-date')
    events = Evenement.objects.all().order_by('-date')
    galeries = Galerie.objects.all().order_by('-date')
    articles = Blog.objects.all().order_by('-date')
    multimedias = Multimedia.objects.all().order_by('-date')
    abouts = About.objects.all()
    context = {'solutions': solutions,
               'slides' : slides,
               'events' : events,
               'galeries' : galeries, 
               'articles' : articles,
               'multimedias' : multimedias, 
               'abouts' : abouts,
               }
    return render(request, 'index.html', context)


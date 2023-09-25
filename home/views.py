from django.shortcuts import render, redirect
from .models import Solutions, Slides
from .models import Evenement, Galerie, Adhesion
from .models import Blog, Multimedia, About

def index(request):
    if request.method == 'POST' and'btn-adhesion' in request.POST:
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        numero = request.POST['numero']
        ville = request.POST['ville']
        presentation = request.POST['presentation']
        new_adhesion = Adhesion(nom=nom, prenom=prenom, numero=numero, ville=ville, presentation=presentation)
        new_adhesion.save()
        return redirect('/')
    
    solutions = Solutions.objects.all().order_by('-date')
    slides = Slides.objects.all().order_by('-date')
    events = Evenement.objects.all().order_by('-date')
    galeries = Galerie.objects.all().order_by('-date')
    articles = Blog.objects.all().order_by('-date')
    multimedias = Multimedia.objects.all().order_by('-date')
    abouts = About.objects.all().order_by('-date')
    context = {'solutions': solutions,
               'slides' : slides,
               'events' : events,
               'galeries' : galeries, 
               'articles' : articles,
               'multimedias' : multimedias, 
               'abouts' : abouts,
               }
    return render(request, 'index.html', context)


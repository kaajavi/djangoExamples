from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
# Create your views here.
from notepad.models import Note

def home(request):
    context = RequestContext(request)
    notas = Note.objects.all()
    context['usuario_actual'] = request.user
    context['notas'] = notas
    return render_to_response("index.html", context)

def nota(request, id_nota):
    context = RequestContext(request)
    nota = Note.objects.get(pk=id_nota)    
    context['nota'] = nota
    return render_to_response("nota.html", context)

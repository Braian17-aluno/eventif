from django.shortcuts import render, redirect
from contact.forms import FormularioContato
from django.http import HttpResponse, HttpResponseRedirect


def contact(request):
    if (request.method == 'POST'):
        return create(request)
    else:
        return new(request)

def create(request):
    form = FormularioContato(request.POST)
    
    if not form.is_valid():
        return render(request, 'contact/contact.html', {'form': form})
    else:
        return HttpResponseRedirect('/contact/')

def new(request):
    return render(request, 'contact/contact.html', {'form': FormularioContato()})

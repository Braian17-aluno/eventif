from django.shortcuts import render, redirect
from contact.forms import FormularioContato
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = FormularioContato(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = FormularioContato()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
  return HttpResponse('Success!')
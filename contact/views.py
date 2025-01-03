from django.http import HttpResponseRedirect
from django.shortcuts import render
from contact.forms import FormularioContato
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from contact.models import Contact
# Create your views here.
def contact(request):
  if(request.method == 'POST'):
    return create(request)
  else:
    return new(request)
    
def create(request):
    form = FormularioContato(request.POST)

    if not form.is_valid():
      return render(request, 'contact/contact.html', {'form': form})

    #mail
    _send_mail(
      'contact/contact_email.txt', 
      form.cleaned_data,
      'Confirmação de contato!', 
      form.cleaned_data['email'],
      settings.DEFAULT_FROM_EMAIL
      )
    
    Contact.objects.create(**form.cleaned_data)

    #message
    messages.success(request, 'Contato realizado com sucesso!')
    return HttpResponseRedirect('/contact/')

def new(request): 
  return render(request, 'contact/contact.html', {'form': FormularioContato()})

def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])

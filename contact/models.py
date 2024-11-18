from django.db import models
from django.forms import Textarea
from django import forms

# Create your models here.
class Contact(models.Model):
  nome = models.CharField('nome', max_length=100)
  telefone = models.CharField('telefone', max_length=20)
  email = models.EmailField('e-mail')
  menssagem = models.CharField('menssagem', max_length=200)



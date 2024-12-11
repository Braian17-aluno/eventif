from django.db import models
from django.db.models.signals import pre_save
from django.apps import AppConfig
from django.core.signals import setting_changed
# Create your models here.

class Contact(models.Model):
  nome = models.CharField('nome', max_length=100)
  telefone = models.CharField('telefone', max_length=20, blank=True)
  email = models.EmailField('e-mail')
  mensagem = models.TextField('mensagem')
  enviado_em = models.DateTimeField('enviado em', auto_now_add=True)
  resposta = models.TextField('resposta', blank=True)
  respondido_em = models.DateTimeField('respondido em', blank=True, null=True)
  resp_check = models.BooleanField('Respondido?', default=False)
  
  class Meta:
    verbose_name_plural = 'contatos'
    verbose_name = 'contato'
    ordering = ('-enviado_em', '-respondido_em')
  
  def __str__(self):
    return self.nome
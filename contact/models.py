from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core import mail
from django.template.loader import render_to_string
from django.conf import settings
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

@receiver(pre_save, sender=Contact)
def contact_response_email(sender, instance, **kwargs):
  if (instance.resposta != '' and instance.resp_check == True):
    data = {'nome': instance.nome, 'telefone': instance.telefone, 'email': instance.email, 'mensagem': instance.mensagem, 'resposta': instance.resposta}                                                                
    def _send_mail(template_name, context, subject, from_, to):
      body = render_to_string(template_name, context)
      email = mail.send_mail(subject, body, from_, [from_, to])
    _send_mail(
        'contact/contact_response.txt', 
        data,
        'Resposta de contato.', 
        settings.DEFAULT_FROM_EMAIL,
        instance.email
        )
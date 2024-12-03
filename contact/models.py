## from django.db import models

# # Create your models here.

# class Contact(models.Model):
#   nome = models.CharField('nome', max_length=100)
#   telefone = models.CharField('telefone', max_length=20, blank=True)
#   email = models.EmailField('e-mail')
#   mensagem = models.TextField('mensagem')
#   #created_at = models.DateTimeField('criado em', auto_now_add=True)
#   #paid = models.BooleanField('pago', default=False)

#   class Meta:
#     verbose_name_plural = 'contatos'
#     verbose_name = 'contato'
#     ordering = ('-created_at',)
  
#   def __str__(self):
#     return self.name
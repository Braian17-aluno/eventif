from django.contrib import admin
from contact.models import Contact
from django.utils.timezone import now
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
  list_display = ('nome', 'telefone', 'email', 'mensagem','enviado_em', 'resposta', 'resp_check', 'respondido_em', 'respondido_hj')
  date_hierarchy = 'enviado_em'
  search_fields = ('nome', 'telefone', 'email', 'mensagem','enviado_em', 'resposta', 'resp_check','respondido_em')
  list_filter = ['enviado_em','respondido_em']
  actions = ['mark_response',]
  def respondido_hj(self, obj):
    if (obj.respondido_em != None):
      return obj.respondido_em.date() == now().date()
  respondido_hj.short_description = 'Respondido hoje?'
  respondido_hj.boolean = True

  def mark_response(self, request, queryset):
    count = queryset.update(resp_check=True)
    if count == 1:
      msg = "{} contato foi marcado como respondido."
    else:
      msg = "{} contatos foram marcados como respondido"
    self.message_user(request, msg.format(count))
  mark_response.short_description = "Marcar como respondido"


admin.site.register(Contact, ContactModelAdmin)
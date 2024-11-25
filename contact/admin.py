from django.contrib import admin
from contact.models import Contact
from django.utils.timezone import now
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
  list_display = ('nome', 'telefone', 'email', 'mensagem','created_at')
  date_hierarchy = 'created_at'
  search_fields = ('nome', 'telefone', 'email', 'mensagem','created_at')
  list_filter = ['created_at']
  #actions = ['mark_as_paid',]
  # def subscribed_today(self, obj):
  #   return obj.created_at.date() == now().date()
  # subscribed_today.short_description = 'Inscrito hoje?'
  # subscribed_today.boolean = True

  # def mark_as_paid(self, request, queryset):
  #   count = queryset.update(paid=True)
  #   if count == 1:
  #     msg = "{} inscrição foi marcada como paga."
  #   else:
  #     msg = "{} inscrições foram marcadas como pagas"
  #   self.message_user(request, msg.format(count))
  # mark_as_paid.short_description = "Marcar como pago"


admin.site.register(Contact, ContactModelAdmin)
from django.test import TestCase
from contact.admin import ContactModelAdmin, Contact, admin
from unittest.mock import Mock

class SubscriptionModelAdminTest(TestCase):
  def setUp(self):
    Contact.objects.create(nome='Braai', telefone='1234567890', email='braai@gmail.com', mensagem='teste')
    self.model_admin = ContactModelAdmin(Contact, admin.site)

  def test_has_action(self):
    self.assertIn('mark_response', self.model_admin.actions)

  def test_mark_all(self):
    self.call_action()
    self.assertEqual(1, Contact.objects.filter(resp_check=True).count())

  def test_mensagem(self):
    mock = self.call_action()
    mock.assert_called_once_with(None,'1 contato foi marcado como respondido.')
  
  def call_action(self):
    queryset = Contact.objects.all()

    mock = Mock()
    old_message_user = ContactModelAdmin.message_user
    ContactModelAdmin.message_user = mock

    self.model_admin.mark_response(None, queryset)

    ContactModelAdmin.message_user = old_message_user

    return mock
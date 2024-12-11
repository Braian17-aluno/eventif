from django.test import TestCase
from datetime import datetime
from contact.models import Contact

class ContactModelTest(TestCase):
  def setUp(self):
    self.obj = Contact(
      nome = 'Braai',
      telefone= '123981371904619',
      email = 'braai@gmail.com',
      mensagem = 'teste'
    )
    self.obj.save()

  def test_create(self):
    self.assertTrue(Contact.objects.exists())

  def test_enviado_em(self):
    self.assertIsInstance(self.obj.enviado_em, datetime)

  def test_str(self):
    self.assertEqual('Braai', str(self.obj))
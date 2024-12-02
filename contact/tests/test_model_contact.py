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

  # def test_create(self):
  #   self.assertTrue(Contact.objects.exists())

  # def test_created_at(self):
  #   self.assertIsInstance(self.obj.created_at, datetime)

  # def test_str(self):
  #   self.assertEqual('Braai', str(self.obj))
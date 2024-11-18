from django.test import TestCase
from contact.forms import FormularioContato
#Create your tests here.

class FormularioContatoTest(TestCase):
  def setUp(self):
    self.form = FormularioContato()

  def test_has_form(self):
    expected = ['nome', 'telefone','email','menssagem' ]
    self.assertSequenceEqual(expected, list(self.form.fields))
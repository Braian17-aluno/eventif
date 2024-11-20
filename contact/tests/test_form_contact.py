from django.test import TestCase
from contact.forms import FormularioContato
#Create your tests here.

class FormularioContatoTeste(TestCase):
  def setUp(self):
    self.form = FormularioContato()

  def test_has_form(self):
    expected = ['nome', 'telefone','email', 'mensagem' ]
    self.assertSequenceEqual(expected, list(self.form.fields))
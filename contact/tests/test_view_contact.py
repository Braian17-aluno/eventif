from django.test import TestCase
from django.core import mail
from contact.forms import FormularioContato
from contact.models import Contact

class ContatoGet(TestCase):
  
  def setUp(self):
    self.response = self.client.get('/contact/')

  def test_get(self):
    self.assertEqual(200, self.response.status_code)
  
  def test_template(self):
    self.assertTemplateUsed(self.response, 'contact/contact.html')
  
  def test_html(self):
    tags = (
      ('<form', 1),
      ('<input', 5),
      ('type="text"', 2),
      ('type="email"', 1),
      ('type="submit"',1),
      ('<textarea',1)
      )
    for text, count in tags:
      with self.subTest():
        self.assertContains(self.response, text, count)
  
  def test_csrf(self):
    self.assertContains(self.response, 'csrfmiddlewaretoken')

class ContatoPostValido(TestCase):
  def setUp(self):
    data = dict(nome="Braai", telefone='53-12345-6789', email='braai@gmail.com', mensagem="Teste")
    self.resp = self.client.post('/contact/', data)

  def test_post(self):
    self.assertRedirects(self.resp,'/contact/')

  def test_send_contact_email(self):
    self.assertEqual(1, len(mail.outbox))

  def test_save_contact(self):
        self.assertTrue(Contact.objects.exists())

class ContatoPostInvalido(TestCase):
  def setUp(self):
    self.resp = self.client.post('/contact/', {})
  
  def test_post(self):
    self.assertEqual(200, self.resp.status_code)
  
  def test_template(self):
    self.assertTemplateUsed(self.resp, 'contact/contact.html')
  
  def test_has_form(self):
    form = self.resp.context['form']
    self.assertIsInstance(form, FormularioContato)

  def test_form_has_error(self):
    form = self.resp.context['form']
    self.assertTrue(form.errors)

  def test_dont_save_contact(self):
        self.assertFalse(Contact.objects.exists())

class ContatoMensagemSucesso(TestCase):
  def test_message(self):
    data = dict(nome="Braai", telefone='53-12345-6789', email='braai@gmail.com', mensagem="Teste")
    resp = self.client.post('/contact/', data, follow=True)
    self.assertContains(resp, 'Contato realizado com sucesso!')

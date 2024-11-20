from django.test import TestCase
from django.core import mail


class ContatoPostValido(TestCase):
  def setUp(self):
    data = dict(nome="Braai", telefone='53-12345-6789', email='braai@gmail.com', mensagem='Teste')
    self.client.post('/contact/', data)
    self.email = mail.outbox[0]

  def test_contact_email_subject(self):
    expect = 'Confirmação de contato!'
    self.assertEqual(expect, self.email.subject)
  
  def test_contact_email_from(self):
    expect = 'braai@gmail.com'
    self.assertEqual(expect, self.email.from_email)
  
  def test_contact_email_to(self):
    expect = ['braai@gmail.com', 'contato@eventif.com.br']
    self. assertEqual(expect, self.email.to)

  def test_contact_email_body(self):
    contents = (
      'Braai',
      '53-12345-6789',
      'braai@gmail.com',
      'Teste',
    )
    for content in contents:
      with self.subTest():
        print(self.email.body)
        self.assertIn(content, self.email.body)
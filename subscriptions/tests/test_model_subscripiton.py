from django.test import TestCase
from datetime import datetime
from subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
  def setUp(self):
    self.obj = Subscription(
      name = 'Braai',
      cpf = '23234234',
      email = 'braai@gmail.com',
      phone= '123981371904619',
    )
    self.obj.save()

  def test_create(self):
    self.assertTrue(Subscription.objects.exists())

  def test_created_at(self):
    self.assertIsInstance(self.obj.created_at, datetime)

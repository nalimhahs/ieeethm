from django.db import models
from .services import get_order

# Create your models here.

class Order(models.Model):
  
  order_id = models.CharField(max_length=30, blank=True)
  razorpay_order_id = models.CharField(max_length=50, blank=True)
  razorpay_payment_id = models.CharField(max_length=50, blank=True)
  razorpay_signature = models.CharField(max_length=50, blank=True)
  amount = models.DecimalField(decimal_places=0, max_digits=7)
  entity = models.CharField(max_length=10, blank=True)
  reciept = models.CharField(max_length=50, blank=True)
  user = models.ForeignKey('main.User', on_delete=models.PROTECT)
  event = models.ForeignKey('main.Event', on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)

  # @classmethod
  def create(cls, User, Event):
    print('here')
    order = cls()
    order_object = get_order(Event)
    order_id = order_object.order_id
    amount = order_object.amount
    entity = order_object.entity
    order.user = User
    order.event = Event
    # order.reciept = "ieeethm#" + order.order_id[6:]
    order.reciept = order_object.reciept
    order.created_at = order_object.created_at
    return order

  def __str__(self):
    return self.reciept
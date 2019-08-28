from django.db import models

# Create your models here.


class Order(models.Model):
  order_id = models.TextField(max_length=30)
  razorpay_order_id = models.TextField(max_length=50)
  razorpay_payment_id = models.TextField(max_length=50, null=True)
  razorpay_signature = models.TextField(max_length=50, null=True)

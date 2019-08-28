from django.db import models

# Create your models here.

class User(models.Model):
  name = models.TextField(max_length=20)
  age = models.DecimalField(decimal_places=0, max_digits=3)

  def __str__(self):
    return self.name

    
class Event(models.Model):
  name = models.TextField(max_length=20)
  amount = models.DecimalField(decimal_places=0, max_digits=7)

  def __str__(self):
    return self.name
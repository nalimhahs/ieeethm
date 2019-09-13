from django.db import models

# Create your models here.

class Catagory(models.Model):
  name = models.CharField(max_length=32)
  desc = models.TextField(max_length=128, null=True)
  thumb = models.URLField(null=True)

  def __str__(self):
    return self.name

class Organizer(models.Model):
  name = models.CharField(max_length=32)
  phone = models.CharField(max_length=32)
  email = models.EmailField()

  def __str__(self):
    return self.name


class Event(models.Model):
  event_id = models.DecimalField(max_digits=3, primary_key=True, decimal_places=0)
  name = models.CharField(max_length=64)
  desc = models.TextField(max_length=1024)
  price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  organizer_1 = models.ForeignKey(Organizer, on_delete=models.PROTECT, related_name='event_organizer_1', null=True, blank=True)
  organizer_2 = models.ForeignKey(Organizer, on_delete=models.PROTECT, related_name='event_organizer_2', null=True, blank=True)
  event_start = models.DateTimeField(null=True, blank=True)
  event_end = models.DateTimeField(null=True, blank=True)
  banner_url = models.URLField(null=True, blank=True)
  catagory = models.ForeignKey(Catagory, on_delete=models.PROTECT, null=True, blank=True)
  reg_link = models.URLField(null=True, blank=True)

  def __str__(self):
    return self.name



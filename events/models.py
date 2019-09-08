from django.db import models

# Create your models here.

class Catagory(models.Model):
  name = models.CharField(max_length=32)

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
  price = models.DecimalField(max_digits=10, decimal_places=2)
  organizer_1 = models.ForeignKey(Organizer, on_delete=models.PROTECT, related_name='event_organizer_1')
  organizer_2 = models.ForeignKey(Organizer, on_delete=models.PROTECT, related_name='event_organizer_2')
  event_start = models.DateTimeField()
  event_end = models.DateTimeField()
  banner_url = models.URLField()
  catagory = models.ForeignKey(Catagory, on_delete=models.PROTECT)
  card_image_url = models.URLField()

  def __str__(self):
    return self.name



from django.db import models
from django.contrib.auth.models import User
from community.models import Manager
from events.models import GuestRun
from rental.models import Reservation

# Create your models here.
class Days(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(GuestRun, on_delete=models.CASCADE)
    reservation_id = models.CharField(max_length=50)
    participant = models.CharField(max_length=20)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return str(self.event.title) + "_"+ str(self.participant)+"_"+ str(self.date)
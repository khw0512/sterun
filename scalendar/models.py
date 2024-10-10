from django.db import models
from django.contrib.auth.models import User
from community.models import Manager
from events.models import GuestRun

# Create your models here.
class Days(models.Model):
    d_id = models.CharField(primary_key=True,max_length=10)
    events = models.CharField(max_length=50)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.d_id + "_"+ str(self.date)
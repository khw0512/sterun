from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField
from community.models import Manager

# def image_upload_path(instance, filename):
#    time = timezone.now()
#    return f"{instance}/{time}+{filename}"

class GuestRun(models.Model):

    STATUS_CHOICE = [
        ("ST1", "Checking"),
        ("ST2", "On-Sale"),
        ("ST3", "Sold-Out"),
        ("ST4", "Closed"),
    ]

    LEVEL = [
        ("Level-1, 800","800"),
        ("Level-2, 730","730"),
        ("Level-3, 700","700"),
        ("Level-4, 630","630"),
        ("Level-5, 600","600"),
        ("Level-6, 530","530"),
        ("Full Access","Free"),
    ]

    event_id = models.AutoField(
        primary_key=True,
    )
    title = models.CharField(max_length=50)
    manager = models.ForeignKey(Manager, related_name="manager",blank=False, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    start_time = models.TimeField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(default=timezone.now)
    image = ResizedImageField(size=[1402,1000], upload_to="runMain", blank=True)
    route_image = ResizedImageField(size=[1402,1402], upload_to="runRoute", blank=True)
    start_point = models.CharField(max_length=50)
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICE,
        default="ST1",
    )
    level = models.CharField(
        max_length=15,
        choices=LEVEL,
        default="Free",
    )
    amount = models.IntegerField(default=0)
    route = models.CharField(max_length=50, blank=False)
    desc = models.TextField(blank=True, default="-")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.completed) + "_" + str(self.status)+"_"+ str(self.manager) + "_" + str(self.title)+"_"+ str(self.event_id)
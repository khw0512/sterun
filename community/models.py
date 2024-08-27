from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class ContactUs(models.Model):

    CATEGORY_CHOICE = [
        ("CG1", "About Event"),
        ("CG2", "About Rental Items"),
        ("CG3", "About Business"),
        ("CG4", "Others"),
    ]

    q_id = models.CharField(
        max_length=20,
        primary_key=True,
        default="Required_pk",
    )
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=False)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICE,
        default="CG1",
    )
    shortq = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.completed) + " " + self.username + "_" + self.q_id
    
class Manager(models.Model):
    m_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(default=0)
    image = ResizedImageField(size=[200,200], upload_to="avatar", blank=False)

    def __str__(self):
        return self.name + "_"+ str(self.m_id)

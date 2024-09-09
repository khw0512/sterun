from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from events.models import GuestRun
from items.models import *

class Reservation(models.Model):

    STATUS_CHOICE = [
        ("ST1", "예약 양식 제출 완료"),
        ("ST2", "예약 완료 및 결제 대기"),
        ("ST3", "결제 완료"),
        ("ST4", "배송 중"),
        ("ST5", "배송 완료"),
        ("ST6", "반납 완료"),
        ("ST7", "입고 완료"),
    ]

    reserv_id = models.CharField(
        max_length=20,
        primary_key=True,
        default="Required_pk",
    )
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=False)
    start_date = models.DateField(blank=True,null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True,null=True)
    end_time = models.TimeField(blank=True, null=True)
    top = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        limit_choices_to={"category": "top"},
        related_name="topName",
        blank=True,
        null=True,
    )
    top_q = models.IntegerField(default=0)
    bottom = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        limit_choices_to={"category": "bottom"},
        related_name="bottomName",
        blank=True,
        null=True,
    )
    bottom_q = models.IntegerField(default=0)
    shoes = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        limit_choices_to={"category": "shoes"},
        related_name="shoesName",
        blank=True,
        null=True,
    )
    bag = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        limit_choices_to={"category": "bag"},
        related_name="bagName",
        blank=True,
        null=True,
    )
    event = models.ForeignKey(
        GuestRun,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    event_date = models.DateField(blank=True,null=True)
    event_time = models.TimeField(blank=True, null=True)
    image = models.ImageField(upload_to="reservation", blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICE,
        default="ST1",
    )
    amount = models.IntegerField(default=0)
    paypal_link = models.CharField(max_length=50, blank=False, default="-")
    delivery = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.completed) + " " + self.username + "_" + self.reserv_id
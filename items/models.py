from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


def image_upload_path(instance, filename):
    time = timezone.now()
    return f"{instance}/{time}+{filename}"


class Item(models.Model):

    CATEGORY = [
        ("shoes", "Shoes"),
        ("top", "Top"),
        ("bottom", "Bottom"),
        ("bag", "Bag & Pouch"),
        ("etc", "ETC"),
    ]

    SIZE = [
        ("Others", "free"),
        (
            "shoes",
            (
                ("220", "220mm"),
                ("225", "225mm"),
                ("230", "230mm"),
                ("235", "235mm"),
                ("240", "240mm"),
                ("245", "245mm"),
                ("250", "250mm"),
                ("255", "255mm"),
                ("260", "260mm"),
                ("265", "265mm"),
                ("270", "270mm"),
                ("275", "275mm"),
                ("280", "280mm"),
                ("285", "285mm"),
                ("290", "290mm"),
                ("295", "295mm"),
                ("300", "300mm"),
            ),
        ),
        (
            "top",
            (
                ("XS", "XS"),
                ("S", "S"),
                ("M", "M"),
                ("L", "L"),
                ("XL", "XL"),
                ("XXL", "XXL"),
            ),
        ),
        (
            "bottom",
            (
                ("XXS", "XXS"),
                ("XS", "XS"),
                ("S", "S"),
                ("M", "M"),
                ("L", "L"),
                ("XL", "XL"),
                ("XXL", "XXL"),
                ("3XL", "3XL"),
                ("4XL", "4XL"),
                ("5XL", "5XL"),
            ),
        ),
    ]

    GENDER = {("M", "Male"), ("F", "Female"), ("E", "NO Gender")}

    category = models.CharField(max_length=10, choices=CATEGORY)
    gender = models.CharField(max_length=1, blank=True, choices=GENDER)
    name = models.CharField(max_length=20, blank=True)
    model_num = models.CharField(primary_key=True, max_length=50, blank=True)
    size = models.CharField(max_length=10, blank=True, choices=SIZE)
    amount = models.IntegerField(default=0, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.model_num

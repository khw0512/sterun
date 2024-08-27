import csv
import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sterun.settings")
django.setup()

from items.models import Item

with open('items.csv') as csv_file:
    rows = csv.reader(csv_file)
    next(rows, None)
    for row in rows:
        print(row)
        Item.objects.create(
            category = row[0],
            gender = row[1],
            name = row[2],
            model_num = row[3],
            size = row[4],
            amount = row[5],
            link = row[6]
        )
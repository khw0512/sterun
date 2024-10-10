import csv
import os
import django
import pandas as pd
import calendar
from datetime import datetime, date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sterun.settings")
django.setup()

from scalendar.models import Days


# Generated by Django 4.2.15 on 2024-08-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0007_alter_guestrun_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guestrun",
            name="status",
            field=models.CharField(
                choices=[
                    ("ST1", "Checking"),
                    ("ST2", "On-Sale"),
                    ("ST3", "Sold-Out"),
                    ("ST4", "Closed"),
                ],
                default="ST1",
                max_length=8,
            ),
        ),
    ]

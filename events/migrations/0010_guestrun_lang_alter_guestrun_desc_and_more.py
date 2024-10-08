# Generated by Django 4.2.15 on 2024-09-04 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0009_alter_guestrun_end_time_alter_guestrun_start_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="guestrun",
            name="lang",
            field=models.CharField(
                choices=[
                    ("KO", "Korean"),
                    ("EN", "English"),
                    ("JP", "Japanese"),
                    ("CN", "Chinese"),
                ],
                default="KO",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="guestrun",
            name="desc",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="guestrun",
            name="level",
            field=models.CharField(
                choices=[
                    ("800", "Level-1, 800"),
                    ("730", "Level-2, 730"),
                    ("700", "Level-3, 700"),
                    ("630", "Level-4, 630"),
                    ("600", "Level-5, 600"),
                    ("530", "Level-6, 530"),
                    ("Free", "Full Access"),
                ],
                default="Free",
                max_length=15,
            ),
        ),
    ]

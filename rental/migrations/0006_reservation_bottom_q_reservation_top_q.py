# Generated by Django 4.2.15 on 2024-09-09 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental", "0005_alter_reservation_end_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="bottom_q",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="reservation",
            name="top_q",
            field=models.IntegerField(default=0),
        ),
    ]
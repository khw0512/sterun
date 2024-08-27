# Generated by Django 4.2.15 on 2024-08-26 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("E", "NO Gender")],
                max_length=1,
            ),
        ),
    ]

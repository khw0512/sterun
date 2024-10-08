# Generated by Django 4.2.15 on 2024-09-04 03:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0011_alter_guestrun_lang"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guestrun",
            name="lang",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("KO", "Korean"),
                    ("EN", "English"),
                    ("JP", "Japanese"),
                    ("CN", "Chinese"),
                ],
                default="KO",
                max_length=10,
            ),
        ),
    ]

# Generated by Django 4.2.15 on 2024-09-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0013_alter_guestrun_lang"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guestrun",
            name="lang",
            field=models.CharField(max_length=10),
        ),
    ]
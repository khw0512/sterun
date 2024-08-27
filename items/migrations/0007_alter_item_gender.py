# Generated by Django 4.2.15 on 2024-08-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0006_alter_item_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("E", "NO Gender"), ("F", "Female")],
                max_length=1,
            ),
        ),
    ]

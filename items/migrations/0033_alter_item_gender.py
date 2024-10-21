# Generated by Django 4.2.15 on 2024-10-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0032_alter_item_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("E", "NO Gender"), ("F", "Female"), ("M", "Male")],
                max_length=1,
            ),
        ),
    ]

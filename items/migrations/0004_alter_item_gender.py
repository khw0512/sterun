# Generated by Django 4.2.15 on 2024-08-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0003_alter_item_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("F", "Female"), ("E", "NO Gender"), ("M", "Male")],
                max_length=1,
            ),
        ),
    ]

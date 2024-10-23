# Generated by Django 4.2.15 on 2024-10-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0052_alter_item_gender"),
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

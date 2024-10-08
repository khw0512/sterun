# Generated by Django 4.2.15 on 2024-10-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0021_alter_item_gender"),
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

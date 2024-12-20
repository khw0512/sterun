# Generated by Django 4.2.15 on 2024-10-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0045_alter_item_gender"),
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

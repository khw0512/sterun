# Generated by Django 4.2.15 on 2024-10-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="days",
            fields=[
                ("d_id", models.AutoField(primary_key=True, serialize=False)),
                ("events", models.CharField(max_length=50)),
                ("date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]

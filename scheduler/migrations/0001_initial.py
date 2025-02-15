# Generated by Django 4.2 on 2023-05-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="faculty",
            fields=[
                (
                    "fac_id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("fac_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="subject",
            fields=[
                (
                    "sub_code",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("sub_name", models.CharField(max_length=100)),
                ("sub_cat", models.CharField(max_length=100)),
                ("fac_1", models.CharField(max_length=10)),
                ("fac_2", models.CharField(max_length=10)),
                ("fac_3", models.CharField(max_length=10)),
                ("room", models.CharField(max_length=10)),
            ],
        ),
    ]

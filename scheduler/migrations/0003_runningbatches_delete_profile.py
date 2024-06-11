# Generated by Django 4.2 on 2023-05-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scheduler", "0002_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="runningbatches",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("batch", models.CharField(max_length=20)),
                ("school", models.CharField(max_length=20)),
                ("division", models.CharField(max_length=20)),
                ("semester", models.CharField(max_length=20)),
                ("nsubs", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
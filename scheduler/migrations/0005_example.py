# Generated by Django 4.2 on 2023-05-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scheduler", "0004_slot_alter_runningbatches_nsubs"),
    ]

    operations = [
        migrations.CreateModel(
            name="example",
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
                ("sname", models.CharField(max_length=5)),
                ("starttime", models.TimeField()),
            ],
        ),
    ]

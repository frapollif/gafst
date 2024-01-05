# Generated by Django 4.2.3 on 2023-10-22 13:10

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompetitionRegistration",
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
                (
                    "status",
                    models.DateField(
                        default=django.utils.datetime_safe.date.today,
                        verbose_name="due_date",
                    ),
                ),
                (
                    "creation_date",
                    models.DateField(
                        default=django.utils.datetime_safe.date.today,
                        verbose_name="creation_date",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="competition",
            name="date",
        ),
        migrations.AddField(
            model_name="competition",
            name="creation_date",
            field=models.DateField(
                default=django.utils.datetime_safe.date.today,
                verbose_name="creation_date",
            ),
        ),
        migrations.AddField(
            model_name="competition",
            name="due_date",
            field=models.DateField(
                default=django.utils.datetime_safe.date.today, verbose_name="due_date"
            ),
        ),
    ]

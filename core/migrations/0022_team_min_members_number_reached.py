# Generated by Django 4.2.3 on 2023-11-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0021_team_min_members_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="min_members_number_reached",
            field=models.BooleanField(
                default=False, verbose_name="min_members_number_reached"
            ),
        ),
    ]

# Generated by Django 4.2.3 on 2023-11-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0017_team_club"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="description",
            field=models.TextField(
                max_length=10000, null=True, verbose_name="description"
            ),
        ),
    ]

# Generated by Django 4.2.3 on 2023-11-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0018_team_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="competition",
            name="description",
            field=models.TextField(
                max_length=10000, null=True, verbose_name="description"
            ),
        ),
    ]

# Generated by Django 4.2.3 on 2023-12-09 17:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0034_competitionregistration_discipline_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Rule",
            new_name="Division",
        ),
    ]
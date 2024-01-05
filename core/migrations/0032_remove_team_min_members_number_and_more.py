# Generated by Django 4.2.3 on 2023-12-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0031_remove_discipline_rules_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="min_members_number",
        ),
        migrations.RemoveField(
            model_name="team",
            name="min_members_number_not_reached",
        ),
        migrations.AlterField(
            model_name="discipline",
            name="max_members_number",
            field=models.IntegerField(
                default=6, null=True, verbose_name="max_members_number"
            ),
        ),
        migrations.AlterField(
            model_name="discipline",
            name="min_members_number",
            field=models.IntegerField(
                default=6, null=True, verbose_name="min_members_number"
            ),
        ),
    ]
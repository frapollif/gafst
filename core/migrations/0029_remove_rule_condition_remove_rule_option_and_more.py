# Generated by Django 4.2.3 on 2023-11-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0028_yearrule"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rule",
            name="condition",
        ),
        migrations.RemoveField(
            model_name="rule",
            name="option",
        ),
        migrations.RemoveField(
            model_name="rule",
            name="value",
        ),
        migrations.AddField(
            model_name="rule",
            name="year_rules",
            field=models.ManyToManyField(
                blank=True, to="core.yearrule", verbose_name="year_rules"
            ),
        ),
    ]
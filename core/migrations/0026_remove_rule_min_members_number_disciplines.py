# Generated by Django 4.2.3 on 2023-11-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0025_rule_min_members_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rule",
            name="min_members_number",
        ),
        migrations.CreateModel(
            name="Disciplines",
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
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "description",
                    models.TextField(
                        max_length=10000, null=True, verbose_name="description"
                    ),
                ),
                (
                    "min_members_number",
                    models.IntegerField(default=6, verbose_name="min_members_number"),
                ),
                (
                    "rules",
                    models.ManyToManyField(
                        blank=True, to="core.rule", verbose_name="rules"
                    ),
                ),
            ],
        ),
    ]
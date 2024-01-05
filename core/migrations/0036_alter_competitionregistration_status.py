# Generated by Django 4.2.3 on 2023-12-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0035_rename_rule_division"),
    ]

    operations = [
        migrations.AlterField(
            model_name="competitionregistration",
            name="status",
            field=models.CharField(
                choices=[
                    ("Draft", "DRAFT"),
                    ("Registered", "REGISTERED"),
                    ("Finished", "FINISHED"),
                ],
                default="Draft",
                max_length=50,
                verbose_name="status",
            ),
        ),
    ]
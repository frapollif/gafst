# Generated by Django 4.2.3 on 2023-09-15 09:35

import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_member_photo_memberchange_photo_alter_exam_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Competition",
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
                ("date", models.DateField(verbose_name="date")),
            ],
        ),
        migrations.AlterField(
            model_name="member",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="photos",
                validators=[
                    core.validators.validate_image_size,
                    django.core.validators.FileExtensionValidator(
                        ["png", "jpg", "jpeg"]
                    ),
                ],
                verbose_name="photo",
            ),
        ),
        migrations.AlterField(
            model_name="memberchange",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="photos",
                validators=[
                    core.validators.validate_image_size,
                    django.core.validators.FileExtensionValidator(
                        ["png", "jpg", "jpeg"]
                    ),
                ],
                verbose_name="photo",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="competitions.html",
            field=models.ManyToManyField(
                blank=True, to="core.competition", verbose_name="competition"
            ),
        ),
        migrations.AddField(
            model_name="memberchange",
            name="competitions.html",
            field=models.ManyToManyField(
                blank=True, to="core.competition", verbose_name="competition"
            ),
        ),
    ]
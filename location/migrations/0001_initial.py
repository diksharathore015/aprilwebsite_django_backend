# Generated by Django 5.1.5 on 2025-01-18 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="city_images/"),
                ),
                ("meta_title", models.CharField(blank=True, max_length=255, null=True)),
                ("meta_description", models.TextField(blank=True, null=True)),
                (
                    "meta_keywords",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("short_description", models.TextField(blank=True, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("facebook", models.URLField(blank=True, null=True)),
                ("instagram", models.URLField(blank=True, null=True)),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("youtube_link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="State",
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
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="state_images/"),
                ),
                ("meta_title", models.CharField(blank=True, max_length=255, null=True)),
                ("meta_description", models.TextField(blank=True, null=True)),
                (
                    "meta_keywords",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("short_description", models.TextField(blank=True, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("facebook", models.URLField(blank=True, null=True)),
                ("instagram", models.URLField(blank=True, null=True)),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("youtube_link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Locality",
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
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="locality_images/"
                    ),
                ),
                ("meta_title", models.CharField(blank=True, max_length=255, null=True)),
                ("meta_description", models.TextField(blank=True, null=True)),
                (
                    "meta_keywords",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("short_description", models.TextField(blank=True, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("facebook", models.URLField(blank=True, null=True)),
                ("instagram", models.URLField(blank=True, null=True)),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("youtube_link", models.URLField(blank=True, null=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="localities",
                        to="location.city",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="city",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cities",
                to="location.state",
            ),
        ),
    ]

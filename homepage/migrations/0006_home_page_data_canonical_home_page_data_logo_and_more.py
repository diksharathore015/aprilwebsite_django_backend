# Generated by Django 5.2 on 2025-04-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0005_home_page_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="home_page_data",
            name="canonical",
            field=models.CharField(
                blank=True,
                help_text="canonical for SEO purposes.",
                max_length=500,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="home_page_data",
            name="logo",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="home_page_data",
            name="meta_description",
            field=models.TextField(
                blank=True,
                help_text="SEO description for the home page, displayed in search engine results.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="home_page_data",
            name="meta_keywords",
            field=models.CharField(
                blank=True,
                help_text="Comma-separated keywords for SEO purposes.",
                max_length=500,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="home_page_data",
            name="meta_title",
            field=models.CharField(
                blank=True,
                help_text="SEO title for the home page, displayed in search engine results.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="home_page_data",
            name="url",
            field=models.CharField(
                blank=True, help_text="url", max_length=500, null=True
            ),
        ),
    ]

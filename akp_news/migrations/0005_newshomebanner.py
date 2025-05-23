# Generated by Django 5.1.6 on 2025-05-12 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "akp_news",
            "0004_remove_news_meta_description_remove_news_meta_image_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsHomeBanner",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "banner_title",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "banner_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="banner_images/"
                    ),
                ),
                (
                    "banner_news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="banner_news",
                        to="akp_news.news",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

# Generated by Django 5.1.6 on 2025-05-13 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akp_news", "0007_news_meta_description_news_meta_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="view_count",
        ),
        migrations.CreateModel(
            name="ViewCountNews",
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
                ("count", models.PositiveIntegerField(default=0)),
                ("ip_addr", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="view_counts",
                        to="akp_news.news",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

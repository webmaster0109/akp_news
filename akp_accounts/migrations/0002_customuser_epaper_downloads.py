# Generated by Django 5.1.6 on 2025-05-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akp_accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="epaper_downloads",
            field=models.PositiveIntegerField(
                default=0, help_text="Number of E-Paper downloads"
            ),
        ),
    ]

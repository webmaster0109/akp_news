# Generated by Django 5.1.6 on 2025-07-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akp_epapers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="epaper",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to="epapers/thumbnails/"
            ),
        ),
    ]

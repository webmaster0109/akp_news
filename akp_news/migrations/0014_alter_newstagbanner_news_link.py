# Generated by Django 5.1.6 on 2025-05-14 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akp_news", "0013_alter_advertisement_banner_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newstagbanner",
            name="news_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]

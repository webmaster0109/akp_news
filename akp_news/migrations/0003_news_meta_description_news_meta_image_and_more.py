# Generated by Django 5.1.6 on 2025-05-12 17:39

import Base.base
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akp_news", "0002_newstagbanner"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="meta_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="news",
            name="meta_image",
            field=models.ImageField(blank=True, null=True, upload_to="meta_images"),
        ),
        migrations.AddField(
            model_name="news",
            name="meta_keywords",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="news",
            name="meta_title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="newscategory",
            name="meta_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newscategory",
            name="meta_image",
            field=models.ImageField(blank=True, null=True, upload_to="meta_images"),
        ),
        migrations.AddField(
            model_name="newscategory",
            name="meta_keywords",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newscategory",
            name="meta_title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="newscomment",
            name="meta_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newscomment",
            name="meta_image",
            field=models.ImageField(blank=True, null=True, upload_to="meta_images"),
        ),
        migrations.AddField(
            model_name="newscomment",
            name="meta_keywords",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newscomment",
            name="meta_title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="newstag",
            name="meta_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newstag",
            name="meta_image",
            field=models.ImageField(blank=True, null=True, upload_to="meta_images"),
        ),
        migrations.AddField(
            model_name="newstag",
            name="meta_keywords",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newstag",
            name="meta_title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="newstagbanner",
            name="meta_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newstagbanner",
            name="meta_image",
            field=models.ImageField(blank=True, null=True, upload_to="meta_images"),
        ),
        migrations.AddField(
            model_name="newstagbanner",
            name="meta_keywords",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newstagbanner",
            name="meta_title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="news",
            name="id",
            field=models.UUIDField(
                default=Base.base.generate_uuid_hex,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="newscategory",
            name="id",
            field=models.UUIDField(
                default=Base.base.generate_uuid_hex,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="newscomment",
            name="id",
            field=models.UUIDField(
                default=Base.base.generate_uuid_hex,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="newstag",
            name="id",
            field=models.UUIDField(
                default=Base.base.generate_uuid_hex,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="newstagbanner",
            name="id",
            field=models.UUIDField(
                default=Base.base.generate_uuid_hex,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]

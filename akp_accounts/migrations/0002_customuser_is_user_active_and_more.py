# Generated by Django 4.2.18 on 2025-06-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akp_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_user_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='verification_otp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='verification_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

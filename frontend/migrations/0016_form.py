# Generated by Django 4.1.3 on 2022-11-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0015_delete_client"),
    ]

    operations = [
        migrations.CreateModel(
            name="Form",
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
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]

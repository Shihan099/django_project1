# Generated by Django 4.1.3 on 2022-11-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0005_alter_about_des"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="des",
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]

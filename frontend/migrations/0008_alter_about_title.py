# Generated by Django 4.1.3 on 2022-11-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0007_remove_about_icon_remove_portfolio_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="title",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
# Generated by Django 4.1.3 on 2022-11-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0017_form_mess_alter_form_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("img", models.ImageField(null=True, upload_to="")),
            ],
        ),
        migrations.DeleteModel(
            name="Form",
        ),
        migrations.AddField(
            model_name="portfolio",
            name="img",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="team",
            name="img_team",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lib_user",
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
                ("uname", models.CharField(max_length=20)),
                ("mobile", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=20)),
                (
                    "pic",
                    models.FileField(
                        default="avtar.webp", null=True, upload_to="st_profile"
                    ),
                ),
            ],
        ),
    ]
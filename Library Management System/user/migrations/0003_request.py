# Generated by Django 4.2.4 on 2023-08-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_user_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Request",
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
                ("title", models.CharField(max_length=30)),
                ("author", models.CharField(max_length=30)),
                ("year", models.CharField(max_length=10)),
                ("deadline", models.CharField(max_length=10)),
            ],
        ),
    ]

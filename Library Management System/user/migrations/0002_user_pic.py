# Generated by Django 4.2.4 on 2023-08-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="pic",
            field=models.FileField(
                default="avtar.webp", null=True, upload_to="profile"
            ),
        ),
    ]

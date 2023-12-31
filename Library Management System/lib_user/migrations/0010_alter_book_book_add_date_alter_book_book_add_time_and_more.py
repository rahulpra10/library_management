# Generated by Django 4.2.4 on 2023-08-13 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lib_user", "0009_alter_book_book_add_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_add_date",
            field=models.DateField(default=datetime.date(2023, 8, 13)),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_add_time",
            field=models.TimeField(
                default=datetime.datetime(
                    2023, 8, 13, 6, 21, 30, 525618, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="issueditem",
            name="issue_date",
            field=models.DateField(default=datetime.date(2023, 8, 13)),
        ),
    ]

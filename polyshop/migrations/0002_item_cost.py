# Generated by Django 4.2.2 on 2023-08-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polyshop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="cost",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polyedu", "0002_verb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_bio",
            field=models.CharField(
                blank=True,
                default="L'écrivain(e) n'a pas de section «À propos».",
                max_length=500,
                null=True,
            ),
        ),
    ]

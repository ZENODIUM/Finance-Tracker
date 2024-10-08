# Generated by Django 5.0.6 on 2024-06-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_financialitem_current_lives"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="financialitem",
            name="budget",
        ),
        migrations.RemoveField(
            model_name="financialitem",
            name="current_lives",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="level_number",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="progress_bar",
            field=models.IntegerField(
                choices=[(1, "1/3"), (2, "2/3"), (3, "3/3")], default=1
            ),
        ),
    ]

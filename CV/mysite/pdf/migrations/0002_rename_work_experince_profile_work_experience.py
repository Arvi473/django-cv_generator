# Generated by Django 4.2.8 on 2024-01-09 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pdf", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile", old_name="work_experince", new_name="work_experience",
        ),
    ]

# Generated by Django 4.2.8 on 2024-01-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("summary", models.TextField(max_length=2000)),
                ("degree", models.CharField(max_length=200)),
                ("school", models.CharField(max_length=200)),
                ("university", models.CharField(max_length=200)),
                ("work_experince", models.TextField(max_length=2000)),
                ("skills", models.TextField(max_length=1000)),
            ],
        ),
    ]

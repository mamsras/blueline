# Generated by Django 5.1.3 on 2024-11-11 19:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("is_admin", models.BooleanField()),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "db_table": "user",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "task_id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("À faire", "À faire"),
                            ("En cours", "En cours"),
                            ("Terminé", "Terminé"),
                        ],
                        default="À faire",
                        max_length=20,
                    ),
                ),
                ("duration", models.DurationField()),
                ("due_date", models.DateTimeField()),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("lastUpdate", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "task",
                "verbose_name_plural": "tasks",
                "db_table": "task",
            },
        ),
    ]

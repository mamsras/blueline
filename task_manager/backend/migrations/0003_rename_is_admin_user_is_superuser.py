# Generated by Django 5.1.3 on 2024-11-12 08:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0002_alter_user_is_admin"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_admin",
            new_name="is_superuser",
        ),
    ]

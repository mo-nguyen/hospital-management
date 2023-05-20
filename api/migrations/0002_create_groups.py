from django.contrib.auth.models import Group
from django.db import migrations

def create_auth_groups(apps, schema_editor):
    Group.objects.bulk_create(
        [
            Group(name="Data Entry Group"),
            Group(name="Diagnostic Group"),
            Group(name="Patient Group"),
        ],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_auth_groups),
    ]
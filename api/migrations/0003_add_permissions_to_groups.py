from django.contrib.auth.models import Group, Permission
from django.db import migrations
from django.contrib.auth.management import create_permissions

def add_permissions_to_group_data_entry(apps, schema_editor):
    app_config = apps.get_app_config("api")
    app_config.models_module = True
    create_permissions(app_config, verbosity=0)
    codenames = [
        "add_enrollment",
        "change_enrollment",
        "view_enrollment",
    ]
    data_entry_group = Group.objects.get(name="Data Entry Group")
    permissions = Permission.objects.filter(codename__in=codenames)
    data_entry_group.permissions.add(*permissions)

def add_permissions_to_group_diagnostic(apps, schema_editor):
    app_config = apps.get_app_config("api")
    app_config.models_module = True
    create_permissions(app_config, verbosity=0)
    codenames = [
        "add_diagnostic_result",
        "change_diagnostic_result",
        "view_diagnostic_result",
    ]
    data_entry_group = Group.objects.get(name="Diagnostic Group")
    permissions = Permission.objects.filter(codename__in=codenames)
    data_entry_group.permissions.add(*permissions)

class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_create_groups"),
    ]

    operations = [
        migrations.RunPython(add_permissions_to_group_data_entry),
        migrations.RunPython(add_permissions_to_group_diagnostic),
    ]
# Generated by Django 3.2.19 on 2023-05-18 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230518_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataelement',
            old_name='code',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='indicator',
            old_name='code',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='organizationunit',
            old_name='uuid',
            new_name='id',
        ),
    ]

# Generated by Django 4.1.6 on 2023-11-21 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_datetoadd_addmembers_datetoadd_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmembers',
            old_name='phoneNumber',
            new_name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='addmembers',
            name='dateToAdd',
        ),
    ]

# Generated by Django 4.1.6 on 2023-11-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_addmembers_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='division',
            field=models.CharField(choices=[('dev', 'dev'), ('cpd', 'cpd')], max_length=200, null=True),
        ),
    ]
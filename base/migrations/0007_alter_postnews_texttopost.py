# Generated by Django 4.1.6 on 2023-11-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_members_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postnews',
            name='texttopost',
            field=models.CharField(max_length=5000),
        ),
    ]

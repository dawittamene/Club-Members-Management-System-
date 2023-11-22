# Generated by Django 4.1.6 on 2023-11-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_postnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('id_number', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
            ],
        ),
    ]

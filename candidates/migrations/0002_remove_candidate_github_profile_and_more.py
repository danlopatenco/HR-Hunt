# Generated by Django 4.2.6 on 2023-10-07 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='github_profile',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='portfolio_website',
        ),
    ]

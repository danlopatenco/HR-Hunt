# Generated by Django 4.2.6 on 2023-10-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_remove_candidate_github_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='position_fit',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_candidate_position_fit'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='position_fit',
        ),
        migrations.AddField(
            model_name='candidate',
            name='position_fit',
            field=models.ManyToManyField(blank=True, to='candidates.jobposition'),
        ),
    ]
# Generated by Django 4.2.5 on 2023-11-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_race_initiative'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='short_name',
            field=models.CharField(null=True),
        ),
        migrations.RemoveField(
            model_name='career',
            name='career_path',
        ),
        migrations.AddField(
            model_name='career',
            name='career_path',
            field=models.ManyToManyField(null=True, to='main.careerpath'),
        ),
    ]
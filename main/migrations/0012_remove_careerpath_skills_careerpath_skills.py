# Generated by Django 4.2.5 on 2023-11-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_career_career_path_alter_careerpath_skills_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='careerpath',
            name='skills',
        ),
        migrations.AddField(
            model_name='careerpath',
            name='skills',
            field=models.CharField(null=True),
        ),
    ]

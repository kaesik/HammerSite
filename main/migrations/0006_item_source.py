# Generated by Django 4.2.5 on 2023-10-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_itemammunition_itemarmour_itemother_itemweapon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='source',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

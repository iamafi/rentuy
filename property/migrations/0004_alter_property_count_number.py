# Generated by Django 4.1.3 on 2022-11-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_remove_property_rating_property_count_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='count_number',
            field=models.PositiveIntegerField(default=0, verbose_name='количество голосов'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profiles/img.png', null=True, upload_to='profiles', verbose_name='фотка'),
        ),
    ]

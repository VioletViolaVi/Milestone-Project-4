# Generated by Django 3.1.2 on 2020-10-30 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20201030_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_us',
            old_name='about_us_part',
            new_name='section',
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_allow_source_last_change_and_last_success_to_be_blank'),
    ]

    operations = [
        migrations.AddField(
            model_name='enclosure',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='enclosure',
            name='medium',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]

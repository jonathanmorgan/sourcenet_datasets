# Generated by Django 2.0.8 on 2018-08-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context_datasets', '0008_auto_20180820_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='family_identifier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

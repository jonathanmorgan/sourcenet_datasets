# Generated by Django 2.0.8 on 2018-08-08 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('context_data', '0006_dataset_unique_identifier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasetidentifier',
            old_name='dataset',
            new_name='data_set',
        ),
    ]

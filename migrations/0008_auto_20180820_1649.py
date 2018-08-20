# Generated by Django 2.0.8 on 2018-08-20 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sourcenet', '0021_article_file_path'),
        ('sourcenet_datasets', '0007_auto_20180808_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetCitationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citation_type', models.CharField(choices=[('mention', 'mention'), ('analysis', 'analysis')], default='analysis', max_length=255)),
                ('article_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sourcenet.Article_Data')),
                ('data_set_citation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sourcenet_datasets.DataSetCitation')),
            ],
        ),
        migrations.AddField(
            model_name='datasetmention',
            name='data_set_citation_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sourcenet_datasets.DataSetCitationData'),
        ),
    ]
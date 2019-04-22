# Generated by Django 2.1.5 on 2019-02-04 19:08

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('context', '0002_work_log_worker'),
        ('sourcenet', '0022_article_data_work_log'),
        ('context_datasets', '0015_auto_20190203_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkDataSetCitationMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True, null=True)),
                ('value_in_context', models.TextField(blank=True, null=True)),
                ('value_index', models.IntegerField(blank=True, default=0, null=True)),
                ('value_length', models.IntegerField(blank=True, default=0, null=True)),
                ('canonical_index', models.IntegerField(blank=True, default=0, null=True)),
                ('value_word_number_start', models.IntegerField(blank=True, default=0, null=True)),
                ('value_word_number_end', models.IntegerField(blank=True, default=0, null=True)),
                ('paragraph_number', models.IntegerField(blank=True, default=0, null=True)),
                ('context_before', models.TextField(blank=True, null=True)),
                ('context_after', models.TextField(blank=True, null=True)),
                ('capture_method', models.CharField(blank=True, max_length=255, null=True)),
                ('uuid', models.TextField(blank=True, null=True)),
                ('uuid_name', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('team_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mention_type', models.CharField(choices=[('mention', 'mention'), ('analysis', 'analysis')], default='mention', max_length=255)),
                ('score', models.FloatField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sourcenet.Article')),
                ('article_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sourcenet.Article_Data')),
                ('data_set_citation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='context_datasets.DataSetCitation')),
                ('data_set_citation_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='context_datasets.DataSetCitationData')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('work_data_set_citation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='context_datasets.WorkDataSetCitation')),
                ('work_log', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='context.Work_Log')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='workdatasetmention',
            name='work_data_set_citation',
        ),
    ]

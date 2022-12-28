# Generated by Django 3.2.12 on 2022-03-09 02:36

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_student_user'),
        ('kb', '0001_initial'),
        ('wallets', '0002_initial'),
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(editable=False, max_length=128, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_timestamp', models.DateTimeField(editable=False, null=True, verbose_name='Deleted timestamp')),
                ('random_slug', models.SlugField(editable=False, unique=True)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated timestamp')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BlockTypeConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_timestamp', models.DateTimeField(editable=False, null=True, verbose_name='Deleted timestamp')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, verbose_name='Updated timestamp')),
                ('value', models.CharField(max_length=128)),
                ('block_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='block.blocktype')),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='block.blockconfigurationkeyword')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlockTransaction',
            fields=[
                ('deposit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wallets.deposit')),
                ('blockPresentation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='block.blockpresentation')),
            ],
            options={
                'abstract': False,
            },
            bases=('wallets.deposit',),
        ),
        migrations.AddField(
            model_name='blockquestionpresentation',
            name='block_presentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.blockpresentation'),
        ),
        migrations.AddField(
            model_name='blockquestionpresentation',
            name='chosen_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='kb.answeroption'),
        ),
        migrations.AddField(
            model_name='blockquestionpresentation',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kb.question'),
        ),
        migrations.AddField(
            model_name='blockquestionpresentation',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kb.topic'),
        ),
        migrations.AddField(
            model_name='blockpresentation',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.block'),
        ),
        migrations.AddField(
            model_name='blockpresentation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='blockconfiguration',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='block.block'),
        ),
        migrations.AddField(
            model_name='blockconfiguration',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='block.blockconfigurationkeyword'),
        ),
        migrations.AddField(
            model_name='blockassignment',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='block.block'),
        ),
        migrations.AddField(
            model_name='blockassignment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='block',
            name='questions',
            field=models.ManyToManyField(blank=True, to='kb.Question'),
        ),
        migrations.AddField(
            model_name='block',
            name='students',
            field=models.ManyToManyField(blank=True, to='students.Student'),
        ),
        migrations.AddField(
            model_name='block',
            name='topic_grade',
            field=models.ForeignKey(help_text='This are the topics covered in this block', on_delete=django.db.models.deletion.PROTECT, to='kb.topicgrade'),
        ),
        migrations.AddField(
            model_name='block',
            name='type_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='block.blocktype'),
        ),
        migrations.CreateModel(
            name='BlockTypeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=128)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='block.blocktype')),
            ],
            options={
                'verbose_name': 'block type Translation',
                'db_table': 'block_blocktype_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]

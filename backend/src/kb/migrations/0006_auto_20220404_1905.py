# Generated by Django 3.2.12 on 2022-04-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0005_auto_20220330_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeroption',
            name='tts_file',
            field=models.FileField(blank=True, null=True, upload_to='tts'),
        ),
        migrations.AlterField(
            model_name='questionttsasset',
            name='tts_file',
            field=models.FileField(blank=True, null=True, upload_to='tts'),
        ),
    ]

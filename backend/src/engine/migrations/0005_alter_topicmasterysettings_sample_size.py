# Generated by Django 3.2.12 on 2022-03-29 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20220322_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicmasterysettings',
            name='sample_size',
            field=models.IntegerField(default=20),
        ),
    ]
# Generated by Django 3.2.12 on 2022-04-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasuretrack', '0006_dailytreasuretransaction_studentdailytreasure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytreasurelevel',
            name='coins_required',
            field=models.PositiveIntegerField(),
        ),
    ]

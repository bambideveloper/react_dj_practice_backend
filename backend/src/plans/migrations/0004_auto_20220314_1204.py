# Generated by Django 3.2.12 on 2022-03-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_auto_20220314_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardianstudentplan',
            name='expired_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='guardianstudentplan',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='guardianstudentplan',
            name='period',
            field=models.CharField(choices=[('MONTHLY', 'Monthly'), ('YEARLY', 'Yearly')], default='MONTHLY', max_length=100),
        ),
        migrations.AddField(
            model_name='guardianstudentplan',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]

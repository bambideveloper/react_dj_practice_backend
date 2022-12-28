# Generated by Django 3.2.12 on 2022-05-04 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0002_badge_type'),
        ('treasuretrack', '0015_alter_weeklytreasurelevel_bonus_badge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklytreasurelevel',
            name='bonus_badge',
        ),
        migrations.AddField(
            model_name='weeklytreasurelevel',
            name='bonus_badge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='badges.badge'),
        ),
    ]

# Generated by Django 3.2.12 on 2022-04-19 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_student_is_new'),
        ('accounting', '0003_alter_account_balance'),
        ('wallets', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementwallet',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='students.student'),
        ),
        migrations.CreateModel(
            name='DailyTreasureWallet',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.account')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='students.student')),
            ],
            options={
                'abstract': False,
            },
            bases=('accounting.account',),
        ),
    ]

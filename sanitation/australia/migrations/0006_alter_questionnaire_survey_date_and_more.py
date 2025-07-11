# Generated by Django 5.2 on 2025-05-11 18:21

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('australia', '0005_alter_questionnaire_survey_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='survey_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='survey_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 5.1.5 on 2025-03-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_student_enrollment_date_student_last_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='end_date',
            field=models.DateTimeField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='module',
            name='start_date',
            field=models.DateTimeField(verbose_name='start date'),
        ),
    ]

# Generated by Django 5.0.7 on 2024-09-01 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_update'),
        ('lessons', '0002_lesson_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='courses.course', verbose_name='Курс'),
        ),
    ]

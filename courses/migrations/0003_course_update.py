# Generated by Django 5.0.7 on 2024-08-18 14:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='update',
            field=models.ManyToManyField(blank=True, null=True, related_name='courses_update', to=settings.AUTH_USER_MODEL, verbose_name='Обновление курса'),
        ),
    ]

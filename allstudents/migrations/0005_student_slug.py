# Generated by Django 5.2 on 2025-04-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allstudents', '0004_alter_student_homepage_alter_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(blank=True, default='royal', null=True, unique=True),
        ),
    ]

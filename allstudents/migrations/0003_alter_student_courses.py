# Generated by Django 5.1.7 on 2025-04-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allstudents', '0002_alter_student_image'),
        ('courses', '0002_course_studentids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='allstudentslist', to='courses.course'),
        ),
    ]

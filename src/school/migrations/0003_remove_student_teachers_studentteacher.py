# Generated by Django 5.1.5 on 2025-01-20 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teachers',
        ),
        migrations.CreateModel(
            name='StudentTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to='school.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to='school.teacher')),
            ],
        ),
    ]

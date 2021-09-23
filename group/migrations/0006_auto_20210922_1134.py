# Generated by Django 3.2.5 on 2021-09-22 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_remove_student_group_id'),
        ('teachers', '0006_rename_teachers_teacher'),
        ('group', '0005_auto_20210922_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='main_teacher',
            field=models.OneToOneField(db_column='main teacher', null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
        migrations.AlterField(
            model_name='group',
            name='main_student',
            field=models.OneToOneField(db_column='main student', null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AlterField(
            model_name='group',
            name='num_of_students',
            field=models.IntegerField(db_column='number of students', default=10),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(db_column='name of group', max_length=100),
        ),
    ]

# Generated by Django 3.2.5 on 2021-09-22 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_auto_20210922_1119'),
        ('students', '0005_alter_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group_id',
            field=models.ForeignKey(db_column='Group ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='group.group'),
        ),
    ]

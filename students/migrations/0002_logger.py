# Generated by Django 3.2.5 on 2021-09-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
                ('execution_time', models.CharField(max_length=100)),
                ('created', models.DateField()),
            ],
        ),
    ]

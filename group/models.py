from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=100, db_column='name of group')
    num_of_students = models.IntegerField(default=10, db_column='number of students')
    main_student = models.OneToOneField('students.Student', null=True,
                                        on_delete=models.CASCADE, db_column='main student')
    main_teacher = models.OneToOneField('teachers.Teacher', null=True,
                                        on_delete=models.CASCADE, db_column='main teacher')

    def __str__(self):
        return self.title

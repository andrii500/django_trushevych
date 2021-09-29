from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, db_column='first name')
    last_name = models.CharField(max_length=100, db_column='last name')
    age = models.IntegerField(default=18, db_column='age')
    phone = models.CharField(max_length=13, db_column='phone')

    group_id = models.ForeignKey('group.Group', null=True, on_delete=models.CASCADE,
                                 db_column='group id')

    def __str__(self):
        return f"{self.id}. {self.last_name} {self.first_name}"


class Logger(models.Model):
    method = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    execution_time = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.path} - {self.created}"

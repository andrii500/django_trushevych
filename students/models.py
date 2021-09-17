from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.age}"


class Logger(models.Model):
    method = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    execution_time = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.path} - {self.created}"

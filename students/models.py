from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.age}"

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    age = models.IntegerField(default=25)

    def __str__(self):
        return f"{self.id}. {self.last_name} {self.first_name}"

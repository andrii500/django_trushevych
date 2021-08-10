from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=100)
    num_of_students = models.IntegerField(default=10)

    def __str__(self):
        return self.title

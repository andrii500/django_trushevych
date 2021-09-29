from django.core.management.base import BaseCommand
from faker import Faker
from teachers.models import Teacher
from students.models import Student
from students.views import fake_phone_number
from group.models import Group


class Command(BaseCommand):
    help = 'Generate teachers'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        faker = Faker()

        for i in range(options['number_of_teachers']):
            teacher = Teacher(first_name=faker.first_name(), last_name=faker.last_name(), age=faker.random_int(25, 100),
                              subject=faker.random_element(elements=('math',
                                                                     'physics',
                                                                     'history',
                                                                     'literature',
                                                                     'chemistry')))
            teacher.save()

            group = Group(title=teacher.subject)
            group.save()

            result = []
            for student in range(faker.random_int(1, 10)):
                student = Student(first_name=faker.first_name(),
                                  last_name=faker.last_name(),
                                  age=faker.random_int(18, 100),
                                  phone=fake_phone_number(faker),
                                  group_id=group)
                result.append(student)

            Student.objects.bulk_create(result)
            main_student = Student.objects.filter(group_id=group.id).first()

            group.num_of_students = len(result)
            group.main_teacher = teacher
            group.main_student = main_student
            group.save()

        self.stdout.write(self.style.SUCCESS('Successfully created teachers'))

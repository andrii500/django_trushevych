from django.core.management.base import BaseCommand
from faker import Faker
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate teachers'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        faker = Faker()
        result = []

        for i in range(options['number_of_teachers']):
            result.append(Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=faker.random_int(25, 100),
                subject=faker.random_element(
                    elements=('math', 'physics', 'history', 'literature', 'chemistry'))
            ))
        Teacher.objects.bulk_create(result)

        self.stdout.write(self.style.SUCCESS('Successfully created teachers'))

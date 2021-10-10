from celery import shared_task
from faker import Faker
from datetime import datetime, timedelta
from .models import Student, Logger
from django.core.mail import send_mail


faker = Faker()


def fake_phone_number(fake):
    return f'+380{fake.msisdn()[4:]}'


@shared_task
def create_random_students(total):
    result = []

    for _ in range(total):
        result.append(Student(first_name=faker.first_name(),
                              last_name=faker.last_name(),
                              age=faker.random_int(18, 100),
                              phone=fake_phone_number(faker)
                              ))
    Student.objects.bulk_create(result)

    return f"{total} random students created with success!"


# @shared_task
# def beat():
#     print('beat START')
#     sleep(5)
#     print('beat END')


@shared_task
def log_cleaner():
    # logs = Logger.objects.filter(created__lte=datetime.now() - timedelta(days=7)).all()
    # if logs:
    #     logs.delete()
    #     return 'Logs for 7 days have been deleted!'
    # else:
    #     return 'You have not logs older than 7 days!'
    pass


@shared_task
def send_email(title, message, email_from):
    # send_mail(
    #     title,
    #     message,
    #     email_from,
    #     ['vitalik1996@gmail.com'],
    #     fail_silently=False,
    # )
    #
    # return 'E-mail was sent!'
    pass

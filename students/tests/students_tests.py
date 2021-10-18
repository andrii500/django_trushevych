import pytest
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.test import Client
from django.core.mail import send_mail

from ..models import Student, Logger
from ..forms import GenerateRandomStudentForm, ContactUsForm, StudentForm, phone_number_validation
from ..tasks import create_random_students


@pytest.mark.django_db
def test_admin_user_create():
    User.objects.create_user('admin', '', 'admin')
    assert User.objects.count() == 1


def test_index_view():
    response = Client().get('')
    assert response.status_code == 200
    assert '<table class="table">' in response.content.decode()


@pytest.mark.django_db
def test_students_list_view():
    response = Client().get('/students/')
    assert response.status_code == 200
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_generate_student_view():
    Client().get('/generate-student/')
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_generate_students_view():
    Client().get('/generate-students/?count=10')
    assert Student.objects.count() == 10


@pytest.mark.django_db
def test_create_student_form_view():
    Client().post('/create-student/', data={'first_name': 'Andrii',
                                            'last_name': 'T',
                                            'age': 27,
                                            'phone': '+380906006060'})
    assert Student.objects.count() == 1
    assert Student.objects.filter(first_name='Andrii', last_name='T', age=27, phone='+380906006060')


@pytest.mark.django_db
def test_edit_student_view():
    Client().post('/create-student/', data={'first_name': 'Andrii',
                                            'last_name': 'T',
                                            'age': 27,
                                            'phone': '+380906006060'})

    assert '<input type="text" name="first_name" value="Andrii" maxlength="100" required id="id_first_name">' in \
           Client().get('/edit-student/1/').content.decode()

    Client().post('/edit-student/1/', data={'first_name': 'A',
                                            'last_name': 'T',
                                            'age': 27,
                                            'phone': '+380906006060'})

    assert '<input type="text" name="first_name" value="A" maxlength="100" required id="id_first_name">' in \
           Client().get('/edit-student/1/').content.decode()


@pytest.mark.django_db
def test_delete_student_view():
    Client().post('/create-student/', data={'first_name': 'Andrii',
                                            'last_name': 'T',
                                            'age': 27,
                                            'phone': '+380906006060'})
    assert Student.objects.count() == 1

    Client().get('/delete-student/1/')
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_manually_generate_students_form_view():
    response = Client().get('/generate-students-form/')
    assert '<h1>Random student generation form</h1>' in response.content.decode()


def test_sending_email_view():
    response = Client().get('/email-sending-form/')
    assert '<h1>E-mail sending form</h1>' in response.content.decode()
    assert send_mail('hello', 'how are you?', 'example@mail.com', ['example@mail.com'],)


def test_handler404():
    response = Client().get('/wrong_url/')
    assert response.status_code == 404
    assert '<h2>This page was not found check your link.</h2>' in response.content.decode()


def test_student_form():
    form = StudentForm(data={'first_name': 'A', 'last_name': 'T', 'age': 27, 'phone': '+380906006060'})
    assert form.is_valid()


def test_phone_number_validation():
    assert not phone_number_validation('+380906006060')


def test_contact_us_form():
    form = ContactUsForm(data={'title': 'hello', 'message': 'how are you?', 'email_from': 'example@mail.com'})
    assert form.is_valid()


def test_generate_random_student_form():
    form_10 = GenerateRandomStudentForm(data={'total': 10})
    assert form_10.is_valid()
    form_501 = GenerateRandomStudentForm(data={'total': 501})
    assert not form_501.is_valid()


@pytest.mark.django_db
def test_logger():
    Client().get('/admin/')
    assert Logger.objects.count() == 1
    assert Logger.objects.filter(created__lte=datetime.now() - timedelta(days=7)).count() == 0


@pytest.mark.django_db
def test_create_random_students():
    assert create_random_students(10) == '10 random students created with success!'

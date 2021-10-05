import pytest
from django.test import Client

from ..models import Teacher
from ..forms import TeacherFormFromModel


@pytest.mark.django_db
def test_teacher_list_view():
    response = Client().get('/teachers/')
    assert response.status_code == 200
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_create_teacher_form_view():
    Client().post('/create-teacher/', data={'first_name': 'A',
                                            'last_name': 'T',
                                            'subject': 'math',
                                            'age': 27})
    assert Teacher.objects.count() == 1
    assert Teacher.objects.filter(first_name='A', last_name='T', subject='math', age=27)


@pytest.mark.django_db
def test_edit_teacher_view():
    Client().post('/create-teacher/', data={'first_name': 'A',
                                            'last_name': 'T',
                                            'subject': 'math',
                                            'age': 27})

    assert '<input type="text" name="first_name" value="A" maxlength="100" required id="id_first_name">' in \
           Client().get('/edit-teacher/1/').content.decode()

    Client().post('/edit-teacher/1/', data={'first_name': 'A2',
                                            'last_name': 'T',
                                            'subject': 'math',
                                            'age': 27})

    assert '<input type="text" name="first_name" value="A2" maxlength="100" required id="id_first_name">' in \
           Client().get('/edit-teacher/1/').content.decode()


@pytest.mark.django_db
def test_delete_teacher_view():
    Client().post('/create-teacher/', data={'first_name': 'A',
                                            'last_name': 'T',
                                            'subject': 'math',
                                            'age': 27})
    assert Teacher.objects.count() == 1

    Client().get('/delete-teacher/1/')
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_teacher_forms():
    form = TeacherFormFromModel(data={'first_name': 'A', 'last_name': 'T', 'subject': 'math', 'age': 27})
    assert form.is_valid()

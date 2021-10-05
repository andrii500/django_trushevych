import pytest
from django.test import Client

from ..models import Group
# from ..forms import GroupFormFromModel
# from students.models import Student
# from teachers.models import Teacher


@pytest.mark.django_db
def test_group_list_view():
    response = Client().get('/groups/')
    assert response.status_code == 200
    assert Group.objects.count() == 0


# @pytest.mark.django_db
# def test_create_group_form_view():
#     Client().post('/create-student/', data={'first_name': 'A', 'last_name': 'T', 'age': 27, 'phone': '+380906006060'})
#     Client().post('/create-teacher/', data={'first_name': 'A', 'last_name': 'T', 'subject': 'math', 'age': 27})
#     instance_student = Student.objects.get(id=1)
#     instance_teacher = Teacher.objects.get(id=1)
#
#     Client().post('/create-group/', data={'title': 'Group A',
#                                           'num_of_students': 10,
#                                           'main_student': str(instance_student),
#                                           'main_teacher': str(instance_teacher)})
#     assert Group.objects.count() == 1
#     assert Group.objects.filter(title='Group A', num_of_students=10)


@pytest.mark.django_db
def test_create_group_form_view():
    response = Client().get('/create-group/')
    assert response.status_code == 200
    assert '<h2>Group creation form from model</h2>' in response.content.decode()

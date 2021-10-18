import pytest
from django.test import Client

from ..models import Group
from ..forms import GroupFormFromModel
from students.models import Student
from teachers.models import Teacher


@pytest.mark.django_db
def test_group_list_view():
    response = Client().get('/groups/')
    assert response.status_code == 200
    assert Group.objects.count() == 0


@pytest.mark.django_db
def test_create_group_form_view():
    Client().post('/create-student/', data={'first_name': 'A', 'last_name': 'T', 'age': 27, 'phone': '+380906006060'})
    Client().post('/create-teacher/', data={'first_name': 'A', 'last_name': 'T', 'subject': 'math', 'age': 27})
    instance_student = Student.objects.get(id=1)
    instance_teacher = Teacher.objects.get(id=1)

    Client().post('/create-group/', data={'title': 'Group A',
                                          'num_of_students': 10,
                                          'main_student': instance_student.id,
                                          'main_teacher': instance_teacher.id})
    assert Group.objects.count() == 1
    assert Group.objects.filter(title='Group A', num_of_students=10)


@pytest.mark.django_db
def test_edit_group_view():
    Client().post('/create-student/', data={'first_name': 'A', 'last_name': 'T', 'age': 27, 'phone': '+380906006060'})
    Client().post('/create-teacher/', data={'first_name': 'A', 'last_name': 'T', 'subject': 'math', 'age': 27})
    instance_student = Student.objects.get(id=1)
    instance_teacher = Teacher.objects.get(id=1)

    Client().post('/create-group/', data={'title': 'Group A',
                                          'num_of_students': 10,
                                          'main_student': instance_student.id,
                                          'main_teacher': instance_teacher.id})

    assert '<input type="text" name="title" value="Group A" maxlength="100" required id="id_title">' in \
           Client().get('/edit-group/1/').content.decode()

    Client().post('/create-student/', data={'first_name': 'A2', 'last_name': 'T2', 'age': 27, 'phone': '+380906006060'})
    Client().post('/create-teacher/', data={'first_name': 'A2', 'last_name': 'T2', 'subject': 'math', 'age': 27})
    instance_student_2 = Student.objects.get(id=2)
    instance_teacher_2 = Teacher.objects.get(id=2)

    Client().post('/edit-group/1/', data={'title': 'Group B',
                                          'num_of_students': 10,
                                          'main_student': instance_student_2.id,
                                          'main_teacher': instance_teacher_2.id})

    assert '<input type="text" name="title" value="Group B" maxlength="100" required id="id_title">' in \
           Client().get('/edit-group/1/').content.decode()


@pytest.mark.django_db
def test_delete_group_view():
    Client().post('/create-student/', data={'first_name': 'A', 'last_name': 'T', 'age': 27, 'phone': '+380906006060'})
    Client().post('/create-teacher/', data={'first_name': 'A', 'last_name': 'T', 'subject': 'math', 'age': 27})
    instance_student = Student.objects.get(id=1)
    instance_teacher = Teacher.objects.get(id=1)

    Client().post('/create-group/', data={'title': 'Group A',
                                          'num_of_students': 10,
                                          'main_student': instance_student.id,
                                          'main_teacher': instance_teacher.id})
    assert Group.objects.count() == 1

    Client().get('/delete-group/1/')
    assert Group.objects.count() == 0


@pytest.mark.django_db
def test_group_form_from_model():
    Client().post('/create-student/', data={'first_name': 'A', 'last_name': 'T', 'age': 27, 'phone': '+380906006060'})
    Client().post('/create-teacher/', data={'first_name': 'A', 'last_name': 'T', 'subject': 'math', 'age': 27})
    instance_student = Student.objects.get(id=1)
    instance_teacher = Teacher.objects.get(id=1)

    form = GroupFormFromModel(data={'title': 'Math',
                                    'num_of_students': 10,
                                    'main_student': instance_student.id,
                                    'main_teacher': instance_teacher.id})
    assert form.is_valid()

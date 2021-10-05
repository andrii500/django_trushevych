import pytest
from django.core.management import call_command

from ..models import Teacher


@pytest.mark.django_db
def test_generate_teachers_command():
    args = ['50']
    opts = {}
    call_command('generate_teachers', *args, **opts)
    assert Teacher.objects.count() == 50

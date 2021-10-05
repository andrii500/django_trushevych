import pytest
from django.test import Client
from ..models import Exchange
from ..tasks import get_currency_rates


@pytest.mark.django_db
def test_currency_list_view():
    response = Client().get('/currency/')
    assert response.status_code == 200
    assert Exchange.objects.count() == 0
    assert '<title>Exchange List Rates</title>' in response.content.decode()


@pytest.mark.django_db
def test_get_currency_rates():
    assert get_currency_rates() == 'All saved successfully!'


@pytest.mark.django_db
def test_exchange_model():
    cur = Exchange(currency='USD', source='monobank', buy_price=25, sell_price=26)
    cur.save()
    assert Exchange.objects.all().count() == 1
    assert Exchange.objects.get(pk=1).currency == 'USD'

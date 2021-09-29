from django.views.generic import ListView
from .models import Exchange


class ExchangeRateListView(ListView):
    model = Exchange

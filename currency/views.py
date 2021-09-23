from django.shortcuts import render

from .models import Exchange


def list_exchange_rates(request):
    exchange_list = Exchange.objects.all()
    return render(request, 'currency_list.html', {'currency_list': exchange_list})

import requests
from celery import shared_task
from .models import Exchange
from .choices import CURRENCIES


@shared_task
def get_currency_rates():
    response_monobank = requests.get('https://api.monobank.ua/bank/currency')
    response_nationalbank = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

    if response_monobank.status_code == 200:
        for rate in response_monobank.json():
            if str(rate.get('currencyCodeA')) in [currency[0] for currency in CURRENCIES] and\
                    str(rate.get('currencyCodeB')) not in [currency[0] for currency in CURRENCIES]:
                if rate.get('currencyCodeA') == 840:
                    cur_name = 'USD'
                elif rate.get('currencyCodeA') == 978:
                    cur_name = 'EUR'
                currency_monobank = Exchange(
                    currency=cur_name,
                    source='Monobank',
                    buy_price=rate.get('rateBuy', ),
                    sell_price=rate.get('rateSell')
                )
                currency_monobank.save()

    if response_nationalbank.status_code == 200:
        for rate in response_nationalbank.json():
            if rate.get('cc') not in [currency[0] for currency in CURRENCIES]:
                continue
            currency_nationalbank = Exchange(
                currency=rate.get('cc'),
                source='National Bank',
                buy_price=rate.get('rate'),
                sell_price=rate.get('rate')
            )
            currency_nationalbank.save()

    return 'All saved successfully!'

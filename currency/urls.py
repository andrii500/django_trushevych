from django.urls import path
from . import views


urlpatterns = [
    path('exchange/', views.list_exchange_rates, name='list-exchange-rates'),
]

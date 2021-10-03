from django.urls import path
from . import views


urlpatterns = [
    path('currency/', views.ExchangeRateListView.as_view(), name='list-currency-rates'),
]

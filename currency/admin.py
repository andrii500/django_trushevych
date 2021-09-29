from django.contrib import admin

from .models import Exchange


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'currency', 'source', 'buy_price', 'sell_price')
    list_filter = ('currency', 'source')

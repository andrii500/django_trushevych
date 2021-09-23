from django.db import models
from .choices import CURRENCIES


class Exchange(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_column='creation date')
    currency = models.CharField(max_length=10, choices=CURRENCIES, db_column='currency')
    source = models.CharField(max_length=100, db_column='Source')
    buy_price = models.DecimalField(max_digits=10, decimal_places=5, db_column='buy price')
    sell_price = models.DecimalField(max_digits=10, decimal_places=5, db_column='sell price')

    def __str__(self):
        return f"{self.created_at}::{self.currency}, {self.source}; BUY: {self.buy_price}; SELL: {self.sell_price};"

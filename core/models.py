from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    purch_price = models.DecimalField(max_digits=10,decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticker} - {self.name}'
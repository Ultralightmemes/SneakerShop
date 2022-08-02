from django.db import models
from django.contrib.auth.models import User

from sneakers.models import Sneaker, Size


class Order(models.Model):
    sneaker = models.ForeignKey('sneakers.Sneaker', on_delete=models.CASCADE)
    size = models.ForeignKey('sneakers.Size', on_delete=models.CASCADE)
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    STATUS_CHOICES = [
        ('AV', 'Active'),
        ('BO', 'Bought'),
        ('DE', 'Denied'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='AV')

    def __str__(self):
        return self.basket.user.username + ' ' + self.sneaker.__str__()

    def get_status(self):
        for choice in self.STATUS_CHOICES:
            if self.status in choice:
                return choice[1]


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Корзина пользователя ' + self.user.username
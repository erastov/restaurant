from django.db import models
from functools import reduce


class Category(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)


class Subcategory(models.Model):
    name = models.CharField(null=True, max_length=100)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return str(self.name)


class Dish(models.Model):
    name = models.CharField(null=True, max_length=100)
    subcategory = models.ForeignKey(Subcategory)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = 'dishes'
    
    def __str__(self):
        return '{0}, {1}'.format(self.name, self.price)


class Operator(models.Model):
    name = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return str(self.name)


class Restaurant(models.Model):
    name = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return str(self.name)


class Order(models.Model):
    STATUS_CHOICES = (
        ('НПЛ', 'Не оплачен'),
        ('ОПЛ', 'Оплачен'),
        ('ОТМ', 'Отменен'),
    )

    dishes = models.ManyToManyField(Dish)
    operator = models.ForeignKey(Operator)
    restaurant = models.ForeignKey(Restaurant)
    time_of_creation = models.DateTimeField(auto_now_add=True)

    @property
    def cost(self):
        return reduce(lambda accumulation, dish: accumulation + dish.price, self.dishes.all(), 0)

    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='НПЛ',
    )

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.time_of_creation, self.restaurant, self.operator)



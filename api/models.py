from django.db import models


class Category(models.Model):
    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return str(self.name)


class Subcategory(models.Model):
    name = models.CharField(null=True, max_length=100)
    category = models.ForeignKey(Category)

    def __str__(self):
        return str(self.name)


class Dish(models.Model):
    name = models.CharField(null=True, max_length=100)
    subcategory = models.ForeignKey(Subcategory)
    
    def __str__(self):
        return str(self.name)


class Operator(models.Model):
    name = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return str(self.name)


class Restaurant(models.Model):
    name = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return str(self.name)


class Order(models.Model):
    dish = models.ManyToManyField(Dish)
    operator = models.ForeignKey(Operator)
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return str(self.restaurant) + ' ' + str(self.operator)



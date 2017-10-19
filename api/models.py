from django.db import models


class Category(models.Model):

    def __str__(self):
        return str()


class Subcategory(models.Model):
    category = models.ForiegnKey(Category)

    def __str__(self):
        return str()


class Dish(models.Model):
    subcategory = models.ForiegnKey(Subcategory)
    
    def __str__(self):
        return str()


class Operator(models.Model):
    
    def __str__(self):
        return str()


class Restaurant(models.Model):
    
    def __str__(self):
        return str()


class Order(models.Model):
    dish = models.ManyToManyField(Dish)
    operator = models.ForiegnKey(Operator)
    restaurant = models.ForiegnKey(Restaurant)

    def __str__(self):
        return str()



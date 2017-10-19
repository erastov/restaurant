from django.contrib import admin

from .models import Category, Subcategory, Dish, Operator, Restaurant, Order

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Dish)
admin.site.register(Operator)
admin.site.register(Restaurant)
admin.site.register(Order)

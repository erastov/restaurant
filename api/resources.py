from tastypie.resources import ModelResource
from tastypie import fields
from django.http import HttpResponse
from api.models import Category, Subcategory, Dish, Operator, Restaurant, Order


def build_content_type(format, encoding='utf-8'):
    """
    Appends character encoding to the provided format if not already present.
    """
    if 'charset' in format:
        return format

    return "%s; charset=%s" % (format, encoding)


class MyModelResource(ModelResource):
    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.

        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)


class CategoryResource(MyModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        fields = ['name']


class SubcategoryResource(MyModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')

    class Meta:
        queryset = Subcategory.objects.all()
        resource_name = 'subcategory'
        fields = ['name', 'category']


class DishResource(MyModelResource):
    subcategory = fields.ForeignKey(SubcategoryResource, 'subcategory')

    class Meta:
        queryset = Dish.objects.all()
        resource_name = 'dish'
        fields = ['name', 'subcategory', 'price']


class OrderResource(MyModelResource):
    dishes = fields.ManyToManyField(DishResource, 'dishes')

    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        fields = ['dishes', 'time_of_creation', 'cost', 'status']

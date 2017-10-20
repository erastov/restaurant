"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api.resources import OrderResource, DishResource, CategoryResource, SubcategoryResource

order_resource = OrderResource()
dish_resource = DishResource()
category_resource = CategoryResource()
subcategory_resource = SubcategoryResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(order_resource.urls)),
    url(r'^api/', include(category_resource.urls)),
    url(r'^api/', include(subcategory_resource.urls)),
    url(r'^api/', include(dish_resource.urls)),
]

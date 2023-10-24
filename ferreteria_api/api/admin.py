from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Employee)
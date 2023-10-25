from django.urls import path

from .views import *

urlpatterns = [
    path("Pedido/", PedidoViews.as_view()),
    path("Pedido/<int:id>", PedidoViews.as_view()),
    path("Product/", ProductViews.as_view()),
    path("Product/<int:id>", ProductViews.as_view()),
    path("Supplier/", SupplierViews.as_view()),
    path("Supplier/<int:id>", SupplierViews.as_view()),
    path("Category/", CategoryViews.as_view()),
    path("Category/<int:id>", CategoryViews.as_view()),
    path("Person/", PersonViews.as_view()),
    path("Person/<int:id>", PersonViews.as_view()),
    path("Customer/", CustomerViews.as_view()),
    path("Customer/<int:id>", CustomerViews.as_view()),
    path("Employee/", EmployeeViews.as_view()),
    path("Employee/<int:id>", EmployeeViews.as_view()),
]

from django.urls import path

from .views import *

urlpatterns = [
    path("Pedido/", PedidoViews.as_view(), name="pedidos"),
    path("Pedido/<int:id>", PedidoViews.as_view(), name="pedido_id"),
    path("Pedido_detalle/", PedidoDetalleViews.as_view(), name="pedido_detalle"),
    path("Pedido_detalle/<int:id>", PedidoDetalleViews.as_view(), name="pedido_detalle_id"),
    path("Product/", ProductViews.as_view(), name="products"),
    path("Product/<int:id>", ProductViews.as_view(), name="product_id"),
    path("Supplier/", SupplierViews.as_view(), name="suppliers"),
    path("Supplier/<int:id>", SupplierViews.as_view(), name="supplier_id"),
    path("Category/", CategoryViews.as_view(), name="categories"),
    path("Category/<int:id>", CategoryViews.as_view(), name="category_id"),
    path("Person/", PersonViews.as_view(), name="persons"),
    path("Person/<int:id>", PersonViews.as_view(), name="person_id"),
    path("Customer/", CustomerViews.as_view(), name="customers"),
    path("Customer/<int:id>", CustomerViews.as_view(), name="customer_id"),
    path("Employee/", EmployeeViews.as_view(), name="employees"),
    path("Employee/<int:id>", EmployeeViews.as_view(), name="employee_id"),
]

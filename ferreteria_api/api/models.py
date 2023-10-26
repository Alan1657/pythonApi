from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_delete

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.category_name}"


class Person(models.Model):
    person_name_RazonSocial = models.CharField(max_length=200)
    person_apellido_parterno = models.CharField(max_length=200, null=True)
    person_apellido_materno = models.CharField(max_length=200, null=True)
    person_address = models.CharField(max_length=200)
    person_DNI_RUC = models.CharField(max_length=20)
    person_phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.person_name_RazonSocial} - ${self.person_DNI_RUC}"


class Supplier(models.Model):
    Supplier_person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='supplier_person',default=1)

    def __str__(self):
        return f"{self.Supplier_person.person_name_RazonSocial} - ${self.Supplier_person.person_DNI_RUC}"

class Customer(models.Model):
    customer_person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='customer_person')

    def __str__(self):
        return f"{self.customer_person.person_name_RazonSocial} - ${self.customer_person.person_DNI_RUC}"

class Employee(models.Model):
    Employee_cargo = models.CharField(max_length=100)
    Employee_person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='employee_person')
    
    def __str__(self):
        return f"{self.Employee_cargo} - ${self.Employee_person.person_name_RazonSocial}"


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='product_category')
    product_supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name='product_supplier')
    product_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product_name} - ${self.product_brand} - {self.product_price}- {self.product_stock}"

class Pedido(models.Model):
    Employee_pedido = models.ForeignKey(
        Employee, on_delete=models.CASCADE, default=1, related_name='employee_pedido')
    Customer_pedido = models.ForeignKey(
        Customer, on_delete=models.CASCADE, default=1, related_name='customer_pedido')
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.Customer_pedido.customer_person.person_DNI_RUC} - ${self.order_date}"

class Pedido_detalle(models.Model):
    product_pedido = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, default=1, related_name='product_pedido')
    pedido_detalle = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name='pedido_detalle')
    quantity = models.IntegerField()

    @property
    def precio_parcial(self):
        return self.quantity * self.product_pedido.product_price

    def __str__(self):
        return f"{self.product_pedido.product_name} - ${self.product_pedido.product_price} - {self.quantity}- {self.precio_parcial}"


# Define una función para actualizar el stock
@receiver(post_save, sender=Pedido_detalle)
def actualizar_stock(sender, instance, **kwargs):
    # instance es la instancia de Pedido que se acaba de guardar
    producto = instance.product_pedido
    cantidad_vendida = instance.quantity
    producto.product_stock -= cantidad_vendida
    producto.save()


# Conecta la señal post_save al modelo Pedido
post_save.connect(actualizar_stock, sender=Pedido_detalle)

# Define una función para restaurar el stock cuando se elimina un Pedido_detalle
@receiver(post_delete, sender=Pedido_detalle)
def restaurar_stock(sender, instance, **kwargs):
    # instance es la instancia de Pedido_detalle que se acaba de eliminar
    producto = instance.product_pedido
    cantidad_eliminada = instance.quantity
    producto.product_stock += cantidad_eliminada
    producto.save()

# Conecta la señal post_delete al modelo Pedido_detalle
post_delete.connect(restaurar_stock, sender=Pedido_detalle)
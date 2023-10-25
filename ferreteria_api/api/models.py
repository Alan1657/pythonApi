from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.category_name}"


class Supplier(models.Model):
    Supplier_name = models.CharField(max_length=200)
    Supplier_phone = models.CharField(max_length=20)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_brand = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='product_category')
    product_supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name='product_supplier')


class Person(models.Model):
    person_name = models.CharField(max_length=200)
    person_apellido_parterno = models.CharField(max_length=200)
    person_apellido_materno = models.CharField(max_length=200)
    person_address = models.CharField(max_length=200)
    person_DNI = models.CharField(max_length=20)
    person_phone = models.CharField(max_length=20)


class Customer(models.Model):
    customer_person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='customer_person')


class Employee(models.Model):
    Employee_RUC = models.CharField(max_length=20)
    Employee_cargo = models.CharField(max_length=100)
    Employee_person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='employee_person')


class Pedido(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, default=1, related_name='product_pedido')
    order_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.product_name} - ${self.product.product_price} - {self.product.product_quantity}"

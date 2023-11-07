from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.urls import reverse
from .models import Category
from .views import CategoryViews
from .serializers import CategorySerializer

class APITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CategoryViews.as_view()

    def test_get_queryset(self):
        # Crea algunos objetos de prueba en la base de datos
        Category.objects.create(category_name="Category 1")
        Category.objects.create(category_name="Category 2")

        # Crea una instancia de la vista
        view = CategoryViews()

        # Llama al método get_queryset
        queryset = view.get_queryset()

        # Verifica que el queryset retorne todos los objetos de la categoría
        self.assertEqual(queryset.count(), 2)
        self.assertTrue(queryset.filter(category_name="Category 1").exists())
        self.assertTrue(queryset.filter(category_name="Category 2").exists())

    def test_get_category(self):
        category = Category.objects.create(category_name="Test Category")
        request = self.factory.get(reverse("category_id", args=[category.id]))
        response = self.view(request, id=category.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = CategorySerializer(category)
        self.assertEqual(response.data["data"], serializer.data)

    def test_create_category(self):
        data = {"category_name": "Test Category"}
        request = self.factory.post(reverse("categories"), data, format="json")
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().category_name, "Test Category")

    def test_update_category(self):
        category = Category.objects.create(category_name="Test Category")
        updated_data = {"category_name": "Updated Category"}
        request = self.factory.patch(
            reverse("category_id", args=[category.id]), updated_data, format="json")
        response = self.view(request, id=category.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.category_name, "Updated Category")

    def test_delete_category(self):
        category = Category.objects.create(category_name="Test Category")
        request = self.factory.delete(
            reverse("category_id", args=[category.id]))
        response = self.view(request, id=category.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 0)

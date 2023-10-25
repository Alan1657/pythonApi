from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.


class PedidoViews(GenericAPIView):
    serializer_class = PedidoSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Pedido.objects.all()

    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.data
            },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Pedido.objects.get(id=id)
            serializer = PedidoSerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)

        items = Pedido.objects.all()
        serializer = PedidoSerializer(items, many=True)
        return self.get_paginated_response({
            "status": "success",
            "data": self.paginate_queryset(serializer.data)
        })

    def patch(self, request, id=None):
        item = Pedido.objects.get(id=id)
        serializer = PedidoSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Pedido, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Item Deleted"
        })


class ProductViews(GenericAPIView):

    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Product.objects.all()

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.data
            },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Product.objects.get(id=id)
            serializer = ProductSerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)

        items = Product.objects.all()
        serializer = ProductSerializer(items, many=True)
        return self.get_paginated_response({
            "status": "success",
            "data": self.paginate_queryset(serializer.data)
        })

    def patch(self, request, id=None):
        item = Product.objects.get(id=id)
        serializer = ProductSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Product, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Item Deleted"
        })


class SupplierViews(GenericAPIView):
    serializer_class = SupplierSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Supplier.objects.all()

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.data
            },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Supplier.objects.get(id=id)
            serializer = SupplierSerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)

        items = Supplier.objects.all()
        serializer = SupplierSerializer(items, many=True)
        return self.get_paginated_response({
            "status": "success",
            "data": self.paginate_queryset(serializer.data)
        })

    def patch(self, request, id=None):
        item = Supplier.objects.get(id=id)
        serializer = SupplierSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Supplier, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Item Deleted"
        })


class PersonViews(GenericAPIView):
    serializer_class = PersonSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Person.objects.all()

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.data
            },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Person.objects.get(id=id)
            serializer = PersonSerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)

        items = Person.objects.all()
        serializer = PersonSerializer(items, many=True)
        return self.get_paginated_response({
            "status": "success",
            "data": self.paginate_queryset(serializer.data)
        })

    def patch(self, request, id=None):
        item = Person.objects.get(id=id)
        serializer = PersonSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Person, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Item Deleted"
        })


class CustomerViews(GenericAPIView):
    serializer_class = CustomerSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Customer.objects.all()

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.data
            },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Customer.objects.get(id=id)
            serializer = CustomerSerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)

        items = Customer.objects.all()
        serializer = CustomerSerializer(items, many=True)
        return self.get_paginated_response({
            "status": "success",
            "data": self.paginate_queryset(serializer.data)
        })

    def patch(self, request, id=None):
        item = Customer.objects.get(id=id)
        serializer = CustomerSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Customer, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Item Deleted"
        })


class EmployeeViews(GenericAPIView):
    serializer_class = EmployeeSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Employee.objects.all()

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.data
            },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)

        items = Employee.objects.all()
        serializer = EmployeeSerializer(items, many=True)
        return self.get_paginated_response({
            "status": "success",
            "data": self.paginate_queryset(serializer.data)
        })

    def patch(self, request, id=None):
        item = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Employee, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Item Deleted"
        })


class CategoryViews(GenericAPIView):
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Category.objects.all()

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.data
            },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Category.objects.get(id=id)
            serializer = CategorySerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)

        items = Category.objects.all()
        serializer = CategorySerializer(items, many=True)
        return self.get_paginated_response({
            "status": "success",
            "data": self.paginate_queryset(serializer.data)
        })

    def patch(self, request, id=None):
        item = Category.objects.get(id=id)
        serializer = CategorySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            },
                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Category, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Item Deleted"
        })

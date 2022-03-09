from re import search
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.views import View
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
import math

class ProductView(APIView):
    def get(self, request):
        querySearch, queryCategory, queryPage = request.GET.get('search'), request.GET.get('cateogory'), int(request.GET.get('page', 1))
        perPage = 8
        getProducts = Product.objects.all()
        getCategories = Category.objects.all()
        if queryCategory:
            getProducts = getProducts.filter(category__name=queryCategory)
        if querySearch:
            getProducts = getProducts.filter(name__icontains=querySearch)
        total = getProducts.count()
        start = (queryPage - 1) * perPage
        end = queryPage * perPage
        serializer_product = ProductSerializer(getProducts[start:end], many=True)
        serializer_category = CategorySerializer(getCategories, many=True)
        return Response({
            'data': serializer_product.data,
            'categories': serializer_category.data,
            'total': total,
            'page': queryPage,
            'last_page': math.ceil(total / perPage)
        })

from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser
from django_filters import rest_framework as filters
from .models import Product
from .serializers import ProductSerializer

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = filters.CharFilter(field_name="category", lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']

class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
   
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
           
            permission_classes = [AllowAny]
        else:
            
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
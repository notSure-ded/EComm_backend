# products/admin.py

from django.contrib import admin
from .models import Product

# This line tells Django to show the Product model on the admin site.
admin.site.register(Product)
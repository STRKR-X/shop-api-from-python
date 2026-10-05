from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path("products/", ProductListAPIView.as_view()),
    path("products/<int:id>/", ProductDetailAPIView.as_view()),
    
]

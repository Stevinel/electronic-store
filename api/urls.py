from django.urls import path
from .views import ProductGetPost

urlpatterns = [
    path('v1/product/', ProductGetPost.as_view(), name='product'),
]

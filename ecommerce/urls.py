from django.urls import path
from .views import HomeView, ProductListView

#urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('products/', ProductListView.as_view(), name = 'product_list'),
]
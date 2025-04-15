from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
class ProductCreateView(CreateView):
    model = Product
    #form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy('product_list')
class ProductUpdateView(UpdateView):
    model = Product
    #form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete_confirm.html"
    success_url = reverse_lazy('product_list')
    #asdadadasasdasdsadasdsa
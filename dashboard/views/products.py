from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .dashboard import DashboardView
from products.models import Product, Category, Medium
from django.conf import settings


class ProductListView(DashboardView, ListView):
    model = Product
    context_object_name  = 'products'
    template_name = 'dashboard/products/list.html'

class ProductDetailView(DashboardView, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'dashboard/products/details.html'

    def get_context_data(self, **kwargs):
        product_id = self.object.id
        frontend_host = settings.FRONTEND_HOST
        context = super().get_context_data(**kwargs)
        context["product_url"] = f"{frontend_host}/art/{product_id}"
        return context

class CategoryCreateView(DashboardView, CreateView):
    model = Category
    fields = ('name', 'cover_photo')
    template_name =  'dashboard/products/categories/add.html'


    def get_success_url(self):
        messages.success(self.request, "Category Added Successfully")
        return reverse_lazy("dashboard:product_category_details", kwargs = { 'pk': self.object.pk })

class CategoryUpdateView(DashboardView, UpdateView):
    model = Category
    fields = ('name', 'cover_photo')
    template_name =  'dashboard/products/categories/edit.html'


    def get_success_url(self):
        messages.success(self.request, "Category Updated Successfully")
        return reverse_lazy("dashboard:product_category_details", kwargs = { 'pk': self.object.pk })

class CategoryListView(DashboardView, ListView):
    model = Category
    context_object_name = 'categories'
    template_name =  'dashboard/products/categories/list.html'


class CategoryDetailView(DashboardView, DetailView):
    model = Category
    context_object_name = 'category'
    template_name =  'dashboard/products/categories/details.html'

    def get_context_data(self, **kwargs):
        category = self.object.id
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=category)
        return context


from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DeleteView

from categories.models import Category
from profiles.utils import get_profile
from tasks.mixins import AttachProfileMixin


# Create your views here.
class CategoryCreateView(View):
    def get(self, request, *args, **kwargs):
        category_name = kwargs.get("name")
        profile = get_profile()

        Category.objects.get_or_create(
            name=category_name,
            profile=profile
        )

        return redirect("categories:list")

class CategoryListView(AttachProfileMixin, ListView):
    model = Category
    template_name = "categories/category-list.html"
    context_object_name = "categories"

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/category-delete.html"
    context_object_name = "category"
    success_url = "/categories/"



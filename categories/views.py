from django.contrib import messages
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DeleteView

from categories.models import Category
from profiles.mixins import UserAuthenticationMixin
from profiles.utils import get_profile
# from tasks.mixins import AttachProfileMixin


# Create your views here.
class CategoryCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        category_name = kwargs.get("name")
        user = get_user(self.request)

        Category.objects.get_or_create(
            name=category_name,
            user=user
        )

        return redirect("categories:list")

class CategoryListView(UserAuthenticationMixin, ListView):
    model = Category
    template_name = "categories/category-list.html"
    context_object_name = "categories"
    login_message = 'Please log in to view your categories.'

class CategoryDeleteView(UserAuthenticationMixin, DeleteView):
    model = Category
    template_name = "categories/category-delete.html"
    context_object_name = "category"
    success_url = "/categories/"



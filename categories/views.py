
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DeleteView, CreateView

from categories.forms import SubCategoryForm
from categories.models import Category
from profiles.mixins import UserAuthenticationMixin


# Create your views here.
class CategoryCreateView(LoginRequiredMixin, CreateView):

    def get(self, request, *args, **kwargs):
        category_name = kwargs.get("name")

        if category_name:
            Category.objects.get_or_create(
                name=category_name,
                user=request.user
            )
            return redirect("categories:list")

        return render(
            request,
            'categories/category-list.html',
            self.get_context_data()
        )

    def get_context_data(self):
        context = {}

        context['categories'] = Category.objects.filter(
            user=self.request.user
        )

        category_id = self.request.GET.get('category')

        context['selected_category'] = Category.objects.filter(
            pk=category_id,
            user=self.request.user
        ).first()

        context['subcategory_form'] = SubCategoryForm()

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        response = super().form_valid(form)

        category = get_object_or_404(
            Category,
            pk=self.kwargs['pk'],
            user=self.request.user
        )

        self.object.categories.add(category)

        return response

class SubCategoryCreate(LoginRequiredMixin, View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk, user = request.user)

        form = SubCategoryForm()
        return render(
            request,
            'categories/subcategory-form.html',
            {
                'form' : form,
                'category' : category,
            }
        )

    def post(self, request, pk):
        category = get_object_or_404(
            Category,
            pk=pk,
            user=request.user
        )

        form = SubCategoryForm(request.POST)

        if form.is_valid():
            subcategory = form.save()

            category.subcategories.add(subcategory)

            print(f'Sub-category: {subcategory.name}')
            print(f'Category: {category.name}')
            print(category.subcategories.all())

            return redirect('categories:list')

        return render(request, "categories/subcategory-form.html", {
            'form': form,
            'category': category,
        })



# class SubCategoryCreateView(LoginRequiredMixin, View):
#     def post(self, request, category_pk, *args, **kwargs):
#         category = get_object_or_404(
#             Category,
#             pk=category_pk,
#             user=request.user,
#         )
#
#         form = SubCategoryForm(request.POST)
#         if form.is_valid():
#             subcategory = form.save()
#             subcategory.categories.add(category)
#             messages.success(
#                 request,
#                 f"Subcategory '{subcategory.name}' was added to '{category.name}'."
#             )
#             return redirect(f"{reverse('categories:list')}?category={category.pk}")
#
#         messages.error(request, "Please enter a valid subcategory name.")
#         return redirect(f"{reverse('categories:list')}?category={category.pk}")


class CategoryListView(UserAuthenticationMixin, ListView):
    model = Category
    template_name = "categories/category-list.html"
    context_object_name = "categories"
    login_message = 'Please log in to view your categories.'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user).order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get("category")
        cat = Category.objects.filter(
            pk=category_id,
            user=self.request.user,
        ).first()
        context["selected_category"] = cat
        context["sub_selected_category"] = cat.subcategories.all() if cat else None
        print(cat.subcategories.all() if cat else None )

        context["subcategory_form"] = SubCategoryForm()
        return context


class CategoryDeleteView(UserAuthenticationMixin, DeleteView):
    model = Category
    template_name = "categories/category-delete.html"
    context_object_name = "category"
    success_url = "/categories/"



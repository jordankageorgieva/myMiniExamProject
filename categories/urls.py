from django.urls import path

from categories import views

app_name = "categories"

urlpatterns = [
    path("", views.CategoryListView.as_view(), name="list"),
    path("create/<str:name>/", views.CategoryCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="delete"),
    path(
        '<int:pk>/subcategories/add/',
        views.SubCategoryCreate.as_view(),
        name="subcategory-create",
    ),
]
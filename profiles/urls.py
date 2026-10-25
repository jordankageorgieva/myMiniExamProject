
from django.urls import path

from profiles import views

app_name = 'profiles'
urlpatterns = [
    path('', views.login_view, name= 'login'),
    path('details/', views.ProfileUpdateView.as_view(), name = 'details'),
    path('delete/', views.ProfileDeleteView.as_view(), name = 'delete'),
]
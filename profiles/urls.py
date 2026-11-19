from django.contrib.auth.views import LogoutView
from django.urls import path

from profiles import views

app_name = 'profiles'
urlpatterns = [
    path('register/', views.RegisterAppUserView.as_view(), name='register'),
    path('login/', views.LoginAppUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('', views.login_view, name= 'login'),
    path('details/', views.ProfileDetailView.as_view(), name = 'details'),
    path('delete/', views.ProfileDeleteView.as_view(), name = 'delete'),
]
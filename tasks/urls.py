
from django.urls import path, include
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tasks/', include([
        path('create/', views.TaskCreateView.as_view(), name='create'),
        path('<int:pk>/', include([
            path('', views.TaskDetailView.as_view(), name='detail'),
            path('edit/', views.TaskUpdateView.as_view(), name='edit'),
            path('delete/', views.TaskDeleteView.as_view(), name='delete'),
        ])),
    ]))
]
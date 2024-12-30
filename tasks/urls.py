from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]

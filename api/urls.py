from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<int:pk>/', views.taskDetail, name="task-detail"),
    path('task-update/<int:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<int:pk>/', views.taskDelete, name="task-delete"),
    path('task-create/', views.taskCreate, name="task-create")
]
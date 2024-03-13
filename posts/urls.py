from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('delete/<str:pk>', views.delete_blog, name='delete_task'),
    path('update/<str:pk>/', views.update_blog, name='update_blog'),

    path('tasks/list', views.todo, name='list'),
    path("update_task/<str:pk>/", views.updateTask, name="update_task"),
    path("delete/<str:pk>/", views.deleteTask, name="delete_task"),
    path("searchbar/", views.searchbar, name="search_bar"),
]  
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('add-task', views.AddTask, name='add-task'),
    path('update-task<str:pk>/', views.UpdateTask, name='update-task'),
    path('delete-task<str:pk>/', views.DelTask, name='delete-task'),
    path('task<str:pk>/', views.TaskPage, name='task')
]

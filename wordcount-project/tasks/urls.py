from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),   #Class based views
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),   #Class based views
    
    
    path('', views.task, name='tasks'),              #Function based views
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    
]
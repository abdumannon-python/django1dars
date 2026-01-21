from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    # Yangi foydalanuvchi qo'shish uchun (argumentlarsiz)
    path('create_user/', views.CreateView.as_view(), name='create_user'),
    # Tahrirlash uchun (pk bilan)
    path('edit_user/<int:pk>/', views.CreateView.as_view(), name='edit_user'),
    # Detail sahifasi uchun (pk yoki User_id)
    path('detail/<int:User_id>/', views.detail, name='detail'),
]
from django.urls import path,include

from . import views
from .views import create_user

urlpatterns=[
    path('',views.index ,name='index'),
    path('detail/<int:User_id>/',views.detail,name='detail'),
    path('create_user/',views.create_user,name='create_user')
]
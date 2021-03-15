from django.urls import path
from .views import create, read, update, delete
urlpatterns = [
    path('create/', create, name='create'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('', read, name='read'),
]

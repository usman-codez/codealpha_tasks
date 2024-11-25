from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('add/', views.add_stock, name='add_stock'),
    path('remove/', views.remove_stock, name='remove_stock'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('laptops/<int:laptop_id>/', views.laptop_detail, name='laptop_detail'),
]
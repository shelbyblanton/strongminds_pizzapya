from django.urls import path
from . import views

urlpatterns = [
    path('pizza/<int:id>', views.pizza, name="pizza_detail"),
    path('topping/<int:id>', views.topping, name="topping_detail"),
    path('', views.index, name="home"),
]
from django.urls import path
from alumnos import views

urlpatterns = [
    path('home',views.home),
    path('saludo',views.saludo),
]
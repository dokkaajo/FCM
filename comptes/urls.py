from django.urls import path
from .import views

urlpatterns=[
    path('',views.Inscription,name='inscription'),
    path('addCitoyen/', views.CreateCitoyen, name='addCitoyen')

]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name="main"),
    path('list/', views.employee_list, name="list"),
]

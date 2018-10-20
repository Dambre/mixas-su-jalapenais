from django.contrib import admin
from django.urls import path, include
from missions import views

urlpatterns = [
    path('t1/',views.all_missions),
    path('t2/',views.all_missions)
]

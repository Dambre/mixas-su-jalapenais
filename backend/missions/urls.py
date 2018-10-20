from django.contrib import admin
from django.urls import path, include
from missions import views

urlpatterns = [
    path('t1/',views.all_missions),
    path('t2/',views.all_missions),
    path('<id>/',views.mission_by_id),
    path('bycreator/<id>/',views.missions_by_creator),
]


#TODO: FIX PATERN NAMES
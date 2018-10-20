from django.contrib import admin
from django.urls import path, include
from missions import views

urlpatterns = [
    path('', views.all_missions),
    path('<id>/', views.mission_by_id),
    path('by-creator/<id>/',  views.missions_by_creator),
    path('bids', views.bids)
]


#TODO: FIX PATERN NAMES
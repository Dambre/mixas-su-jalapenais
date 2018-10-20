from django.urls import path
from missions import views

urlpatterns = [
    path('', views.all_missions),
    path('<uuid:id>', views.mission_by_id),
    path('by-creator/<uuid:id>/', views.missions_by_creator),
    path('bids', views.bids),
    path('<uuid:id>/bids', views.bids_by_mission_id),
]


#TODO: FIX PATERN NAMES
from django.urls import path
from missions import views


urlpatterns = [
    path('', views.all_missions),
    path('create-mission', views.create_mission),
    path('<uuid:id>', views.get_mission),
    path('<uuid:id>/select-worker', views.select_worker),
    path('<uuid:id>/finish-mission', views.finish_mission),
    path('<uuid:id>/accept_mission',views.accept_mission),
    path('proposed_missions', views.proposed_missions),
]

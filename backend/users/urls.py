from django.urls import path


from . import views

urlpatterns = [
    path('', views.list_users, name='list'),
    path('<uuid:id>', views.user_by_id, name='user_by_id')
]

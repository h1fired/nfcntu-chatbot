from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list),
    path('users/create/', views.user_create_or_get),
    path('users/<int:social_id>/', views.user_detail),
    path('users/update/<int:social_id>/', views.user_update),
]
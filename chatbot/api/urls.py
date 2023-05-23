from django.urls import path
from . import views

urlpatterns = [
    # users
    path('users/', views.users_list, name='api_users_list'),
    path('users/create/', views.user_create_or_get, name='api_user_create'),
    path('users/<int:social_id>/', views.user_detail, name='api_user'),
    path('users/update/<int:social_id>/', views.user_update, name='api_user_update'),
    # contacts
    path('contacts/', views.contact_list, name='api_contacts_list'),
]
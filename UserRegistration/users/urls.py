from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user-registration'),
    path('details/', views.user_details, name='user-details'),
    path('referrals/', views.referrals, name='referrals'),
]

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('shishamaster/', views.check_shisha_master, name='shisha_master'),
    path('shishamaster_check/', views.check_shisha_master, name='check_shisha_master')
]
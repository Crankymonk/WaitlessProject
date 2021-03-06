from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<slug:category_slug>/', views.item_list,
         name='item_list_by_category'),
    path('<slug:slug>/<int:id>/', views.item_detail, name='item_detail'),
    # path('service/about_us/', views.about_us, name='about_us'),
    ]

from django.urls import path
from elevate import views

urlpatterns = [
    
    path('', views.show_page, name=''),
    path('insert_listing', views.listing_form, name='insert_listing'),
    path('all_listings', views.list_all_items, name='all_listings'),
]


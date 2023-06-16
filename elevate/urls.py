from django.urls import path
from elevate import views

urlpatterns = [
    
    path('', views.show_page, name=''),
    path('insert_listing', views.listing_form, name='insert_listing'),
    path('all_listings', views.list_all_items, name='all_listings'),
    path('all_listings/single_listing/<pk>', views.single_listing, name='single_listing'),
]


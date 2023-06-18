from django.urls import path
from elevate import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.show_page, name=''),
    path('insert_listing', views.listing_form, name='insert_listing'),
    path('all_listings', views.list_all_items, name='all_listings'),
    path('all_listings/single_listing/<pk>', views.single_listing, name='single_listing'),
    path('all_listings/single_listing/update_listing/<pk>', views.listing_update, name='update_listing'),
    path('all_listings/single_listing/delete_listing/<pk>', views.listing_delete, name='delete_listing'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

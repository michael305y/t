from django.urls import path
from elevate import views

urlpatterns = [
    
    path('', views.show_page, name=''),
]

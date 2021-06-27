from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactanos', views.contactanos, name='contactanos'),
]

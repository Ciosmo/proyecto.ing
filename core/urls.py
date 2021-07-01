from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('crud', views.abogados, name='abogados'),
    path('form_crud', views.form_crud, name='form_crud'),
    path('mod_form_crud/<id>', views.mod_form_crud, name='mod_form_crud'),
    path('mod_eliminar_crud/<id>', views.mod_eliminar_crud, name='mod_eliminar_crud'),
]

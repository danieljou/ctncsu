from .views import *
from django.urls import path


urlpatterns = [
    path('',index, name = 'home'),

    path("dashboard/", dashboard, name="dashboard"),
    path("organigramme/", organigramme, name="organigramme"),

    path('responsables/create/', responsable_create, name='responsable_create'),
    path('responsables/update/<int:pk>/', responsable_update, name='responsable_update'),
    path('responsables/delete/<int:pk>/', responsable_delete, name='responsable_delete'),

] 

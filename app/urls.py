from .views import *
from django.urls import path


urlpatterns = [
    path('',index, name = 'home'),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("actualite/", actualite, name="actualite"),
    path("organigramme_display/", organigramme_display, name="organigramme_display"),
    path("contacts/", contacts, name="contacts"),

    path("dashboard/", dashboard, name="dashboard"),
    path("organigramme/", organigramme, name="organigramme"),

    path('responsables/create/', responsable_create, name='responsable_create'),
    path('responsables/update/<int:pk>/', responsable_update, name='responsable_update'),
    path('responsables/delete/<int:pk>/', responsable_delete, name='responsable_delete'),
    path("article_create/", article_create, name="article_create"),
    path("manuel_de_procedure/", Manuel_de_procédures, name="Manuel_de_procédures"),
    path("download_pdf/", download_pdf, name="download_pdf"),
    path("<slug:article_slug>/", article_details, name="article_details"),
    

] 

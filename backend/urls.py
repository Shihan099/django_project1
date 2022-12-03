from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="dashboard"),

    # service url
    path('services/', all_services, name="all_services"),
    path('services/add/', add_service, name="add_service"),
    path('services/edit/<int:id>', edit_service, name="edit_services"),

    path('portfolio/', all_portfolio, name="all_portfolio"),
    path('portfolio/add/', add_portfolio, name="add_portfolio"),
    path('portfolio/edit/<int:id>', edit_portfolio, name="edit_portfolio"),

    path('about/', all_about, name="all_about"),
    path('about/add/', add_about, name="add_about"),
    path('about/edit/<int:id>', edit_about, name="edit_about"),

    path('team/', all_team, name="all_team"),
    path('team/add/', add_team, name="add_team"),
    path('team/edit/<int:id>', edit_team, name="edit_team"),

    path('contact/', all_contact, name="all_contact"),
    path('contact/add/', add_contact, name="add_contact"),
    path('contact/edit/<int:id>', edit_contact, name="edit_contact"),

]

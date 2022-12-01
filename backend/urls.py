from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="dashboard"),

    #service url
    path('services/', all_services, name="all_services"),
    path('services/add/', add_service, name="add_service"),
    path('services/edit/<int:id>', edit_service, name="edit_services"),

]
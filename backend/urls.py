from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="dashboard"),
    path('services/', all_services, name="all_services"),

]
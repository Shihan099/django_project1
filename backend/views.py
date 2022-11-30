from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'backend/home.html')


# service starts here
def all_services(request):
    return render(request, 'backend/service/list.html')


def add_service(request):
    return render(request, 'backend/service/add.html')

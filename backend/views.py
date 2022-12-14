from django.shortcuts import render

#frontend local
from frontend.models import Service

# Create your views here.
def index(request):
    return render(request, 'backend/home.html')


# service starts here
def all_services(request):
    services = Service.objects.all()

    context = {
        'all_services': services
    }
    return render(request, 'backend/service/list.html', context)


def add_service(request):
    return render(request, 'backend/service/add.html')


def edit_service(request):
    return render(request, 'backend/service/add.html')


def all_portfolio(request):
    return render(request, 'backend/portfolio/list.html')


def add_portfolio(request):
    return render(request, 'backend/portfolio/add.html')


def edit_portfolio(request):
    return render(request, 'backend/portfolio/add.html')


def all_about(request):
    return render(request, 'backend/about/list.html')


def add_about(request):
    return render(request, 'backend/about/add.html')


def edit_about(request):
    return render(request, 'backend/about/add.html')


def all_team(request):
    return render(request, 'backend/team/list.html')


def add_team(request):
    return render(request, 'backend/team/add.html')


def edit_team(request):
    return render(request, 'backend/team/add.html')


def all_contact(request):
    return render(request, 'backend/contact/list.html')


def add_contact(request):
    return render(request, 'backend/contact/add.html')


def edit_contact(request):
    return render(request, 'backend/contact/add.html')

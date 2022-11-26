from django.shortcuts import render

# local
from frontend.models import *


def home(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    about = About.objects.all()
    team = Team.objects.all()
    client = Client.objects.all()
    footer = Footer.objects.all()

    context = {
        'all_service': services,
        'all_portfolios': portfolio,
        'all_about': about,
        'all_team': team,
        'all_client': client,
        'all_footer': footer,

    }

    return render(request, "index.html", context)





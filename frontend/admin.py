from django.contrib import admin
from frontend.models import Service
from frontend.models import Portfolio
from frontend.models import About
from frontend.models import Team
from frontend.models import Client
from frontend.models import Footer


# Register your models here.


admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Client)
admin.site.register(Footer)


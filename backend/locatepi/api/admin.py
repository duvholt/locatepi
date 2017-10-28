from django.contrib import admin
from .models import Server, Ping

admin.site.register(Server)
admin.site.register(Ping)

from django.contrib import admin
from .models import *

class PoliceModelAdmin(admin.ModelAdmin):
    list_display = ["email", "f_name", "l_name", "rank"]
admin.site.register(PoliceModel, PoliceModelAdmin)


class PoliceAdminModelAdmin(admin.ModelAdmin):
    list_display = ["email", "f_name", "l_name", "rank"]
admin.site.register(PoliceHeadModel, PoliceAdminModelAdmin)

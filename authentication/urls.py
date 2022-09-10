from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path('add-police/', views.addPoliceOfficers, name="add-police-officers"),
	path('add-police-head/', views.addPoliceAdminOfficers, name="add-police-head-officers"),
	path('add-individual-police/', views.addPoliceIndivisualOfficer, name="add-individual-police-officers"),

    path('police-login/', views.login, name="police-login"),
	path('police-forgot/', views.forgot, name="police-forgot"),
	path('police-reset/', views.reset, name="police-login"),

	path('notify-all-police/', views.specialEmail, name="notify-all-police"),

    path('police-head-login/', views.admin_login, name="police-head-login"),
	path('police-head-forgot/', views.admin_forgot, name="police-head-forgot"),
	path('police-head-reset/', views.admin_reset, name="police-head-login"),

]
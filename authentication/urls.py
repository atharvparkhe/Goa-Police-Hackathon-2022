from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path('add-police/', views.addPoliceOfficers, name="add-police-officers"),
	path('add-police-head/', views.addPoliceAdminOfficers, name="add-police-head-officers"),
	
    path('police-login/', views.login, name="police-login"),
	path('police-forgot/', views.forgot, name="police-forgot"),
	path('police-reset/', views.reset, name="police-login"),
	
    # path('police-head-login/', views.police_head_login, name="police-head-login"),
	# path('police-head-forgot/', views.police_head_forgot, name="police-head-forgot"),
	# path('police-head-reset/', views.police_head_reset, name="police-head-login"),
	
]
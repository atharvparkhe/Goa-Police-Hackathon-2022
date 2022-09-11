from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path('categories/', views.GetCategories.as_view(), name="categories"),
	path('add-categories/', views.AddCategories.as_view(), name="add-categories"),
	path('edit-delete-categories/<id>/', views.CategoriesRUD.as_view(), name="edit-delete-categories"),

	# path('search-cases/', views.searchCases, name="search-cases"),

	path('other-cases/', views.OthersCasesLC.as_view(), name="other-cases"),
	path('abuse-cases/', views.AbuseCasesLC.as_view(), name="abuse-cases"),
	path('intoxication-cases/', views.IntoxicationCaseLC.as_view(), name="intoxication-cases"),
	path('aggression-cases/', views.AggresssionCaseLC.as_view(), name="aggression-cases"),
	path('motor-incident-cases/', views.MotorIncidentCaseLC.as_view(), name="motor-incident-cases"),
	path('exploitation-cases/', views.ExploitationCaseLC.as_view(), name="exploitation-cases"),
	
	# path('admin-dashboard/', views.dashboard, name="admin-dashboard"),

]
from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path('categories/', views.GetCategories.as_view(), name="categories"),
	path('add-categories/', views.AddCategories.as_view(), name="add-categories"),
	path('edit-delete-categories/<id>/', views.CategoriesRUD.as_view(), name="edit-delete-categories"),

	path('register-case/', views.AddCases.as_view(), name="register-cases"),
	path('register-person/', views.AddPerson.as_view(), name="register-person"),
	
	path('rescent-cases/', views.RescentCases.as_view(), name="rescent-cases"),
	
	path('search-case/', views.searchCases, name="search-cases"),

]
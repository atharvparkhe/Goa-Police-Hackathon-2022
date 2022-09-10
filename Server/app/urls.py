from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path('categories/', views.GetCategories.as_view(), name="categories"),
	path('add-categories/', views.AddCategories.as_view(), name="add-categories"),
	path('edit-delete-categories/<id>/', views.CategoriesRUD.as_view(), name="edit-delete-categories"),

	# path('add-cases/', views.addCases, name="add-cases"),
	# path('search-cases/', views.searchCases, name="search-cases"),

	

	# path('admin-dashboard/', views.dashboard, name="admin-dashboard"),

]
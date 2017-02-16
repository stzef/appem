from django.conf.urls import patterns, include, url
from infa_web.apps.restaurante_menus.views import *

from django.contrib.auth.decorators import login_required

#url(r'^articles/$', login_required(ArticleList.as_view()), name = 'list-articles'),
urlIngredients = [
	url(r'^ingredients/$', IngredientsList.as_view(), name = 'list-ingredients'),
	url(r'^ingredients/get-list/$', Ingredients_list, name = 'ingrediends_list'),
	url(r'^ingredients/add/$', IngredientCreate.as_view(), name = 'add-ingredient'),
	url(r'^ingredients/edit/(?P<pk>\d+)/$', IngredientUpdate.as_view(), name = 'edit-ingredient'),
]

urlDishes = [
	url(r'^dishes/$', DishesList.as_view(), name = 'list-dishes'),
	url(r'^dishes/add/$', DishCreate.as_view(), name = 'add-dish'),
	url(r'^dishes/edit/(?P<pk>\d+)/$', DishUpdate.as_view(), name = 'edit-dish'),

	url(r'^dishes/ingredients/(?P<pk>\d+)/$', GetDishDetail, name = 'get-ingredients-dish'),
	url(r'^dishes/ingredients/$', DishDetailCRUD, name = 'crud-ingredient-dish'),
]

urlMenu = [
	url(r'^menus/$', MenusList.as_view(), name = 'list-menus'),
	url(r'^menus/add/$', MenuCreate.as_view(), name = 'add-menu'),
	url(r'^menus/edit/(?P<pk>\d+)/$', MenuUpdate.as_view(), name = 'edit-menu'),

	url(r'^menus/dishes/(?P<pk>\d+)/$', GetMenuDetail, name = 'get-platos-menu'),
	url(r'^menus/dishes/$', MenuDetailCRUD, name = 'crud-platos-menu'),
]


urlGroups = [
	#url(r'^menus/groups/$', GroupsList.as_view(), name = 'list-groups-menus'),
	#url(r'^menus/groups/add/$', GroupCreate.as_view(), name = 'add-group-menu'),
	#url(r'^menus/groups/edit/(?P<pk>\d+)/$', GroupUpdate.as_view(), name = 'edit-group-menu'),
]

urlGroups = [
	url(r'^menu-groups/$', GroupList.as_view(), name = 'list-menu-groups'),
	url(r'^menu-groups/add/$', GroupCreate.as_view(), name = 'add-menu-group'),
	url(r'^menu-groups/edit/(?P<pk>\d+)/$', GroupUpdate.as_view(), name = 'edit-menu-group'),
]

urlpatterns = urlIngredients + urlDishes + urlMenu + urlGroups

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
]

urlpatterns = urlIngredients + urlDishes
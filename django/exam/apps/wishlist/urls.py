from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^main$', views.gateway),
	url(r'^register$', views.register),
	url(r'^dashboard$', views.dashboard),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^add_item$', views.add_item),
	url(r'^wish_items/create$', views.create),	
	url(r'^wish_items/add$', views.create),	
	url(r'^wish_items/(?P<item_id>\d+)$', views.wish_items),	
	url(r'^wish_items/(?P<item_id>\d+)/delete$', views.delete),
]
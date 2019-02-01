from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^users$', views.index),
	url(r'^users/new$', views.createRender),
	url(r'^users/create$', views.create),
	
	url(r'^users/(?P<user>\d+)/destroy$', views.destroy),
	url(r'^users/(?P<user>\d+)/edit$', views.updateRender),
	url(r'^users/(?P<user>\d+)/update$', views.update),
	
	url(r'^users/(?P<user>\d+)$',views.read)
]
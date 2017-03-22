from django.conf.urls import url
from django.contrib import admin
from . import views # This line is new!
from ..users import views
urlpatterns = [
  url(r'^$', views.index), # This line has changed!
  url(r'^register/', views.register),
  url(r'^signin/', views.signin),
  url(r'^create/', views.create),
  url(r'^login/', views.login),
  url(r'^logoff/', views.logoff),
  url(r'^create_new/', views.create_new),
  url(r'^users/(?P<id>\d+)$', views.profile),
  url(r'^users/add/(?P<id>\d+)$', views.add_friend),
  url(r'^users/remove/(?P<id>\d+)$', views.remove_friend),
  url(r'^friends$', views.friends)
]

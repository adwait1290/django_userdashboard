from django.conf.urls import url
from django.contrib import admin
from . import views # This line is new!

urlpatterns = [
  url(r'^$', views.dashboard),
  url(r'^admin/', views.admin),
]

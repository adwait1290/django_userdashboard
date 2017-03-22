from django.conf.urls import url
from django.contrib import admin
from . import views # This line is new!

urlpatterns = [
  url(r'^remove/(?P<id>\d+)', views.remove),
  url(r'^edits/', views.edit),
  url(r'^edit_info/', views.editInfo),
  url(r'^edit_password/', views.editPassword),
  url(r'^edit_description/', views.editDescription),
  url(r'^new_user/', views.new_user),
  url(r'^edit/(?P<id>\d+)', views.editAdmin),
  url(r'^specific_edit_info/(?P<id>\d+)', views.specificEditInfo),
  url(r'^specific_edit_password/(?P<id>\d+)', views.specificEditPassword),
  url(r'^show/(?P<id>\d+)', views.profile),
  url(r'^show/post_message/(?P<id>\d+)', views.post_message),
  url(r'^show/post_comment/(?P<id>\d+)/(?P<id2>\d+)', views.post_comment),
  url(r'^users/(?P<id>\d+)$', views.profile),
  url(r'^users/add/(?P<id>\d+)$', views.add_friend),
  url(r'^users/remove/(?P<id>\d+)$', views.remove_friend),
]

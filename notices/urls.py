
from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.notices_list, name='notices_list'),]

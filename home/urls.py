from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^login/$', login, {'template_name' : 'home/login.html'}),
   url(r'^logout/$', logout, {'template_name' : 'home/logout.html'}),
   url(r'^register/$', logout, {'template_name' : 'home/register.html'}),
]
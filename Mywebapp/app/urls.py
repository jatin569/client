from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index,name="index1"),
  url(r'^registration/$',views.reg,name='reg1'),
  url(r'^login/$', views.login, name='login1'),
  url(r'^logout/$', views.logout, name='logout1'),
  url(r'^about/$', views.about, name='about'),
  url(r'^blog/$', views.blog, name='blog'),
  url(r'^contact/$', views.contact, name='contact'),
  url(r'^services/$', views.services, name='services'),
  url(r'^single/$', views.single, name='single'),
  url(r'^work/$', views.work, name='work'),
    ]
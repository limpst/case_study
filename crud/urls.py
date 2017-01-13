from django.conf.urls import patterns, url

from crud import views

urlpatterns = [
    url(r'^$', views.cashflow_list, name='cashflow_list'),
    url(r'^new$', views.cashflow_create, name='cashflow_new'),
    url(r'^edit/(?P<pk>\d+)$', views.cashflow_update, name='cashflow_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.cashflow_delete, name='cashflow_delete'),
    
 #   url(r'^$', views.deal_list, name='deal_list'),
 #   url(r'^new$', views.deal_create, name='deal_new'),
 #   url(r'^edit/(?P<pk>\d+)$', views.deal_update, name='deal_edit'),
 #   url(r'^delete/(?P<pk>\d+)$', views.deal_delete, name='deal_delete'),
    
]

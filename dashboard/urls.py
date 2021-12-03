from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns=[
    path('',views.home,name='dashboard-home'),
    path('co_workingspace/', views.co_workingspace, name='co_workingspace'),
    path('icons_errands/', views.icons_errands, name='icons_errands'),
    path('icons_escapades/', views.icons_escapades, name='icons_escapades'),
    path('icons_events/', views.icons_events, name='icons_events'),
    path('icons_marketing/', views.icons_marketing, name='icons_marketing'),
    path('dashboard_kenya/', views.dashboard_kenya, name='dashboard_kenya'),
    path('icons_whatsapp/', views.icons_whatsapp, name='icons_whatsapp'),
    path('icons_youtube/', views.icons_youtube, name='icons_youtube')

]
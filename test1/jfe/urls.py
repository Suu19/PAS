from jfe import views
from django.urls import path
from django.contrib import admin

urlpatterns=[
    path("homepage/<int:id>",views.HomePageView,name='home'),
    path('', views.aboutPageView,name=''),
    path('list',views.listPageView,name='list')
]
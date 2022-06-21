from jfeWeb import views
from django.urls import path

urlpatterns=[
    path('',views.homeView,name='home'),
    path('list/<str:id>',views.listView,name='list'),
   # path("detail/<str:id>",views.detailView,name='detail'),
    path("detail/<int:id>",views.detailView,name='detail'),
]